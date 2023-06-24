from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid
from sqlalchemy.sql.sqltypes import DateTime

class Incidents(Base):
	__tablename__ = "Incidents"
	id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
	type = Column(Integer)
	body = Column(String)
	title = Column(String)
	sector = Column(UUID(as_uuid=True), ForeignKey("Sector.id"))
	date = Column(DateTime, default=datetime.utcnow)
	
class Incident_type(Base):
	__tablename__ = "Incident_type"
	id = Column(Integer, primary_key=True, index=True)
	name = Column(String)
	
class Weather(Base):
	__tablename__ = "Weather"
	id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
	type = Column(Integer, ForeignKey("Weather_type.id"))
	name = Column(String)
	field = Column(UUID(as_uuid=True), ForeignKey("Field.id"))
	date = Column(DateTime, default=datetime.utcnow)
	
class Weather_type(Base):
	__tablename__ = "Weather_type"
	id = Column(Integer, primary_key=True, index=True)
	name = Column(String)
	
class Sensor(Base):
	__tablename__ = "Sensor"
	id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
	type = Column(Integer)
	value = Column(Integer)
	coordination = Column(String)
	sector = Column(UUID(as_uuid=True), ForeignKey("Sector.id"))
	date = Column(DateTime, default=datetime.utcnow, nullable=True)
	
class Sensor_Type(Base):
	__tablename__ = "Sensor_type"
	id = Column(Integer, primary_key=True, index=True)
	name = Column(String)