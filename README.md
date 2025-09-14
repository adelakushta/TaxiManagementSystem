# Taxi Driver Management System

A FastAPI-based backend service for managing taxi drivers with full CRUD functionality, CSV data persistence, and auto-generated API documentation.


--- 


## Technologies Used

- Python 3.10+
- FastAPI - Modern web framework for building - Uvicorn - ASGI server for running the application
- Pandas - Data manipulation and CSV operations
- Pydantic - Data validation and serialization

---

## Project Structure
```bash
TaxiManagementSystem/
├── app/
│   ├── persistance/
│   │   ├── db/
│   │   │   ├── __init__.py
│   │   │   └── driver_data.py           # CSV data operations with Pandas
│   │   │   └── drivers.csv              # CSV data storage file
│   │   └── models/
│   │       ├── __init__.py
│   │       └── driver_model.py          # Data entity models
│   ├── service/
│   │   ├── __init__.py
│   │   └── driver_service.py            # Business logic layer
│   ├── web/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── controllers/
│   │   │   ├── __init__.py
│   │   │   └── driver_controller.py     # API route handlers
│   │   └── models/
│   │       ├── __init__.py
│   │       └── driver_schema.py         # Pydantic request/response schemas
├── venv/                                # Virtual environment (not included in repo)
├── LICENSE
├── requirements.txt
├── .gitignore
└── README.md
```
---

## Features

- **Driver Entity** with the following properties:
  - `id`: integer (auto-generated, unique identifier)
  - `name`: string
  - `license_number`: string
  - `vehicle_type`: enum (optional)- Sedan, SUV, Van, Coupe, Convertible, Truck, Minivan
  - `is_available`: boolean (default:true)

- **CRUD API Endpoints**


| Method | Endpoint             | Description              | Request Body            |
|--------|----------------------|--------------------------|-------------------------|
| POST   | /drivers             | Create a new driver      | Driver details (no ID)  |
| GET    | /drivers/{driver_id} | Get driver by ID         | None                    |
| PUT    | /drivers/{driver_id} | Update existing driver   | Complete driver details |
| GET    | /drivers             | Get drivers with filters | Query parameters        |


- **Filtering Support**
  - By availability (`is_available`)
  - By vehicle type (`vehicle_type`)
  - By name (case-insensitive)

- **Data Validation**
    - Unique license number enforcement
    - Enum validation for vehicle types
    - Type safety with Pydantic models

---

## Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/adelakushta/TaxiManagementSystem

2. Create & activate a virtual environment (recommended)
    ```bash
    python -m venv venv
    .\venv\Scripts\activate   # On Windows
    source venv/bin/activate # On macOS/Linux

3. Install dependencies
    ```bash
    pip install -r requirements.txt

4. Run the FastAPI server
    ```bash
    # Method 1: Using uvicorn directly
    uvicorn app.web.main:app --reload --host 127.0.0.1 --port 8000
    # Method 2: Using Python
    python -m app/main.py

5. Access the API documentation
    - Swagger UI: http://127.0.0.1:8000/docs
    - ReDoc: http://127.0.0.1:8000/redoc

---

## Usage Examples 

1. Create Driver
    ```bash
    curl -X POST "http://127.0.0.1:8000/drivers" \
    -H "Content-Type: application/json" \
    -d '{
        "name": "John Doe",
        "license_number": "DL123456789",
        "vehicle_type": "sedan",                  
        "is_available": true
    }'

2. Filter Drivers
    ```bash
    # Available drivers only
    curl -X GET "http://127.0.0.1:8000/drivers?is_available=true"
    ```
    ```bash
    # By vehicle type
    curl -X GET "http://127.0.0.1:8000/drivers?vehicle_type=sedan"
    ```
    ```bash
    # By name (partial match)
    curl -X GET "http://127.0.0.1:8000/drivers?name=John"
    ```
    ```bash
    # Multiple filters
    curl -X GET "http://127.0.0.1:8000/drivers?is_available=true&vehicle_type=sedan"
    
3. Get Specific Driver by ID
    ```bash
    curl -X GET "http://127.0.0.1:8000/drivers/1" \ -H "accept: application/json"

4. Update Driver Information
    ```bash 
    curl -X PUT "http://127.0.0.1:8000/drivers/1" \
    -H "Content-Type: application/json" \
    -d '{
        "name": "John Smith",
        "license_number": "DL123456789",
        "vehicle_type": "SUV",
        "is_available": false
    }'
    
---

## Data Management

- Storage: Driver records stored in a CSV file, managed via Pandas DataFrames.
- Auto-generated IDs: Sequential integer IDs starting from 1, incremented for each new driver.
- Data Persistence: Reads always load from CSV; create, update, and delete operations save changes back to CSV.
- Data Validation: Pydantic models enforce field types and integrity.
- Duplicate Prevention: License numbers must be unique.

---

## Available Vehicle Types

The following vehicle types are supported:

- Sedan
- SUV
- Van
- Coupe
- Convertible
- Truck
- Minivan

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
Adela Kushta - adelakushta05@gmail.com
Project Link: https://github.com/adelakushta/TaxiManagementSystem
