from enum import Enum
from pydantic import BaseModel
from typing import Optional


class VehicleType(str, Enum):
    sedan = "Sedan"
    suv = "SUV"
    van = "Van"
    coupe = "Coupe"
    convertible = "Convertible"
    truck = "Truck"
    minivan = "Minivan"


class DriverCreate(BaseModel):
    name: str
    license_number: str
    vehicle_type: Optional[VehicleType] = None
    is_available: bool = True


class DriverUpdate(DriverCreate):
    pass


class DriverResponse(DriverCreate):
    id: int
