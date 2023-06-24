from fastapi import APIRouter, HTTPException, Depends
from typing import List
from src.sensor.repository import SensorRepository
from database import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from src.sensor.schema import Sensor, Sensor_db, Sensor_type, Sensor_type_db, Incident, Incident_db, Weather, Weather_db, Weather_type, Weather_type_db, Role, Role_db
router = APIRouter(prefix="/sensor", tags=["sensor"])

@router.get("/", response_model=List[Sensor_db])
async def get_all(session: AsyncSession = Depends(get_async_session)):
    try:
        sensors = await SensorRepository.get_all(session)
        return sensors
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.post("/", response_model=Sensor)
async def create(sensor: Sensor, session: AsyncSession = Depends(get_async_session)):
    try:
        sensor = await SensorRepository.create(session, sensor)
        return sensor
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.post("/sensor_type", response_model=Sensor_type)
async def create(sensor_type: Sensor_type, session: AsyncSession = Depends(get_async_session)):
    try:
        sensor_type = await SensorRepository.create_sensor_type(session, sensor_type)
        return sensor_type
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.post("/incident", response_model=Incident)
async def create(incident: Incident, session: AsyncSession = Depends(get_async_session)):
    try:
        incident = await SensorRepository.create_incident(session, incident)
        return incident
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.post("/weather", response_model=Weather_db)
async def create(weather: Weather, session: AsyncSession = Depends(get_async_session)):
    try:
        weather = await SensorRepository.create_weather(session, weather)
        return weather
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.post("/weather_type")
async def create(weather_type: Weather_type, session: AsyncSession = Depends(get_async_session)):
    try:
        weather_type = await SensorRepository.create_weather_type(session, weather_type)
        return weather_type
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/sensor_type")
async def get_all(session: AsyncSession = Depends(get_async_session)):
    print("get_all")
    try:
        sensor_types = await SensorRepository.get_all_sensor_type(session)
        print(sensor_types)
        return sensor_types
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/incident", response_model=List[Incident_db])
async def get_all(session: AsyncSession = Depends(get_async_session)):
    try:
        incidents = await SensorRepository.get_all_incident(session)
        return incidents
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/weather", response_model=List[Weather_db])
async def get_all(session: AsyncSession = Depends(get_async_session)):
    try:
        weathers = await SensorRepository.get_all_weather(session)
        return weathers
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/weather_type", response_model=List[Weather_type_db])
async def get_all(session: AsyncSession = Depends(get_async_session)):
    try:
        weather_types = await SensorRepository.get_all_weather_type(session)
        return weather_types
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/{sensor_id}", response_model=Sensor_db)
async def get_by_id(sensor_id: int, session: AsyncSession = Depends(get_async_session)):
    try:
        sensor = await SensorRepository.get_by_id(session, sensor_id)
        return sensor
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))