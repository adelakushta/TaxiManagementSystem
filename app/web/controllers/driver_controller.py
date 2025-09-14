from fastapi import APIRouter, HTTPException
from fastapi import Query
from typing import Optional
from typing import List
from app.service import driver_service
from app.web.models.driver_schema import DriverCreate, DriverUpdate, DriverResponse, VehicleType


router = APIRouter(prefix="/drivers", tags=["drivers"])


@router.post("", response_model=DriverResponse)
def create_driver(driver: DriverCreate):
    try:
        return driver_service.create_driver(driver)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/{driver_id}", response_model=DriverResponse)
def update_driver(driver_id: int, driver: DriverUpdate):
    try:
        updated = driver_service.update_driver(driver_id, driver)
        if not updated:
            raise HTTPException(status_code=404, detail="Driver not found")
        return updated
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{driver_id}", response_model=DriverResponse)
def get_driver(driver_id: int):
    driver = driver_service.get_driver(driver_id)
    if not driver:
        raise HTTPException(status_code=404, detail="Driver not found")
    return driver



@router.get("", response_model=List[DriverResponse])
def get_drivers(
    is_available: Optional[bool] = Query(None),
    vehicle_type: Optional[VehicleType] = Query(None),
    name: Optional[str] = Query(None)
):
    # Convert enum to string value for service layer
    vehicle_type_str = vehicle_type.value if vehicle_type else None
    return driver_service.get_drivers(is_available, vehicle_type_str, name)

