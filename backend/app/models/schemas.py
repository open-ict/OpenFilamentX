from pydantic import BaseModel, Field


class SensorData(BaseModel):
    temperature: float = Field(..., description="Extruder temperature in C")
    diameter: float = Field(..., description="Filament diameter in mm")
    speed: float = Field(..., description="Extrusion speed in mm/s")


class MachineStatus(BaseModel):
    temperature: float
    diameter: float
    speed: float
    quality: str
