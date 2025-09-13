class DriverModel:
    def __init__(self, id: int, name: str, license_number: str, vehicle_type: str, is_available: bool):
        self.id = id
        self.name = name
        self.license_number = license_number
        self.vehicle_type = vehicle_type
        self.is_available = is_available

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "license_number": self.license_number,
            "vehicle_type": self.vehicle_type,
            "is_available": self.is_available,
        }
