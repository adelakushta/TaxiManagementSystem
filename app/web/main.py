import uvicorn
from fastapi import FastAPI

from app.web.controllers import driver_controller

app = FastAPI(
    title="Taxi Driver Management API",
    description="A CRUD API for managing taxi drivers"
)

# include routes
app.include_router(driver_controller.router)


@app.get("/")
def root():
    return {"message": "Welcome to Taxi Driver Management System"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=False)
