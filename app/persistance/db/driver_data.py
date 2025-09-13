import pandas as pd
import os 

FILE_PATH = "drivers.csv"


def load_data():
    if os.path.exists(FILE_PATH):
        try:
            df = pd.read_csv(FILE_PATH)
            if not df.empty:
                # Ensure correct data types
                df['id'] = pd.to_numeric(df['id'], errors='coerce').fillna(0).astype(int)
                df['is_available'] = df['is_available'].apply(lambda x: True if x in [True, 'True', 1, '1'] else False)
                df['name'] = df['name'].astype(str)
                df['license_number'] = df['license_number'].astype(str)
                df['vehicle_type'] = df['vehicle_type'].where(pd.notna(df['vehicle_type']), None)
            return df
        except Exception as e:
            print(f"Error reading CSV: {e}")
            # If file is corrupted, don’t wipe it — raise instead
            raise
    # No file yet → start fresh
    return pd.DataFrame(columns=["id", "name", "license_number", "vehicle_type", "is_available"])


def save_data(df):
    try:
        df.to_csv(FILE_PATH, index=False, mode="w")  # overwrite with updated df
    except Exception as e:
        raise Exception(f"Failed to save data: {e}")