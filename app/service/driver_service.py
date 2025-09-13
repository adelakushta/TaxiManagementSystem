import pandas as pd
from typing import Optional

from app.persistance.db.driver_data import load_data, save_data
from app.persistance.models.driver_model import DriverModel
from app.web.models.driver_schema import DriverCreate, DriverUpdate


def create_driver(driver: DriverCreate):
    # Check for duplicate license numbers
    df = load_data()
    if not df.empty and driver.license_number in df["license_number"].values:
        raise ValueError("License number already exists")

    new_id = 1 if df.empty else int(df["id"].max()) + 1
    new_driver = DriverModel(
        new_id,
        driver.name,
        driver.license_number,
        driver.vehicle_type.value if driver.vehicle_type else None,  # Handle enum
        bool(driver.is_available)
    )
    df = pd.concat([df, pd.DataFrame([new_driver.to_dict()])], ignore_index=True)
    save_data(df)
    return new_driver.to_dict()


def update_driver(driver_id: int, driver: DriverUpdate):
    df = load_data()
    if df.empty or driver_id not in df["id"].values:
        return None

    # Check for duplicate license numbers (excluding current driver)
    existing_license = df[(df["license_number"] == driver.license_number) & (df["id"] != driver_id)]
    if not existing_license.empty:
        raise ValueError("License number already exists for another driver")

    df.loc[df["id"] == driver_id, ["name", "license_number", "vehicle_type", "is_available"]] = [
        driver.name,
        driver.license_number,
        driver.vehicle_type.value if driver.vehicle_type else None,  # Handle enum
        driver.is_available
    ]
    save_data(df)
    return df.loc[df["id"] == driver_id].to_dict(orient="records")[0]


def get_driver(driver_id: int):
    df = load_data()
    if df.empty:
        return None
    driver = df.loc[df["id"] == driver_id]
    if driver.empty:
        return None
    return driver.to_dict(orient="records")[0]


def get_drivers(is_available: Optional[bool] = None, vehicle_type: Optional[str] = None, name: Optional[str] = None):
    df = load_data()
    
    if is_available is not None:
        df = df[df["is_available"] == is_available]
    if vehicle_type is not None:
        df = df[df["vehicle_type"] == vehicle_type]
    if name is not None:
        df = df[df["name"].str.contains(name, case=False, na=False)]

    # Ensure correct types for response
    result = []
    for _, row in df.iterrows():
        driver_dict = {
            "id": int(row["id"]),
            "name": str(row["name"]) if pd.notna(row["name"]) else "",
            "license_number": str(row["license_number"]) if pd.notna(row["license_number"]) else "",
            "vehicle_type": str(row["vehicle_type"]) if pd.notna(row["vehicle_type"]) else None,
            "is_available": bool(row["is_available"])
        }
        result.append(driver_dict)

    return result
