from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.sensor.model import Sensor as SensorModel
from src.sensor.model import Sensor_Type as SensorTypeModel
from src.sensor.model import Incidents as IncidentModel
from src.sensor.model import Weather as WeatherModel
from src.sensor.model import Weather_type as WeatherTypeModel
from src.sensor.schema import Sensor, Sensor_db, Sensor_type, Sensor_type_db, Incident, Incident_db, Weather, Weather_db, Weather_type, Weather_type_db
from typing import List

class SensorRepository():

    async def get_all(session: AsyncSession) -> List[Sensor_db]:
        sensors = await session.execute(select(SensorModel))
        res = sensors.scalars().all()
        res = [Sensor_db(**r.__dict__) for r in res]
        return res
    
    async def get_by_id(session: AsyncSession, sensor_id: int) -> Sensor_db:
        sensor = await session.get(SensorModel, sensor_id)
        return Sensor_db(**sensor.__dict__)
    
    async def create(session: AsyncSession, sensor: Sensor) -> Sensor_db:
        sensor = SensorModel(**sensor.dict())
        session.add(sensor)
        await session.commit()
        await session.refresh(sensor)
        return Sensor_db(**sensor.__dict__)
    
    async def create_sensor_type(session: AsyncSession, sensor_type: Sensor_type) -> Sensor_type_db:
        sensor_type = SensorTypeModel(**sensor_type.dict())
        session.add(sensor_type)
        await session.commit()
        await session.refresh(sensor_type)
        sensor_type = Sensor_type_db(**sensor_type.__dict__)
        return sensor_type

    async def create_incident(session: AsyncSession, incident: Incident) -> Incident_db:
        incident = IncidentModel(**incident.dict())
        session.add(incident)
        await session.commit()
        await session.refresh(incident)
        return Incident_db(**incident.__dict__)
    
    async def create_weather(session: AsyncSession, weather: Weather) -> Weather_db:
        weather = WeatherModel(**weather.dict())
        session.add(weather)
        await session.commit()
        await session.refresh(weather)
        weather = Weather_db(**weather.__dict__)
        return weather
    
    async def create_weather_type(session: AsyncSession, weather_type: Weather_type):
        weather_type1 = WeatherTypeModel(**weather_type.dict())
        session.add(weather_type1)
        await session.commit()
        await session.refresh(weather_type1)
        return weather_type1
    
    async def get_all_sensor_type(session: AsyncSession) -> List[Sensor_type_db]:
        sensor_types = await session.execute(select(SensorTypeModel))
        res = sensor_types.scalars().all()
        print(res)
        res = [Sensor_type_db(**r.__dict__) for r in res]
        return res
    
    async def get_all_incident(session: AsyncSession) -> List[Incident_db]:
        incidents = await session.execute(select(IncidentModel))
        res = incidents.scalars().all()
        res = [Incident_db(**r.__dict__) for r in res]
        return res
    
    async def get_all_weather(session: AsyncSession) -> List[Weather_db]:
        weather = await session.execute(select(WeatherModel))
        res = weather.scalars().all()
        res = [Weather_db(**r.__dict__) for r in res]
        return res
    
    async def get_all_weather_type(session: AsyncSession) -> List[Weather_type_db]:
        weather_types = await session.execute(select(WeatherTypeModel))
        res = weather_types.scalars().all()
        res = [Weather_type_db(**r.__dict__) for r in res]
        return res