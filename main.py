from fastapi import FastAPI
from database import create_tables
from fastapi.middleware.cors import CORSMiddleware
from src.user.router import router as user_router
from src.field.router import router as field_router
from src.task.router import router as task_router
from src.sensor.router import router as sensor_router

app = FastAPI(
    title = "ВИНОвные"
)

@app.on_event("startup")
async def startup():
    print("Starting up...")
    await create_tables()

@app.on_event("shutdown")
async def shutdown():
    print("Shutting down...")

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

app.include_router(user_router)
app.include_router(field_router)
app.include_router(task_router)
app.include_router(sensor_router)