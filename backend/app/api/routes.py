from fastapi import APIRouter
from app.models.schemas import MachineStatus, SensorData
from app.services.quality import evaluate_quality

router = APIRouter()
LATEST_STATE: dict[str, float | str] = {
    "temperature": 0.0,
    "diameter": 0.0,
    "speed": 0.0,
    "quality": "unknown",
}


@router.get("/status", response_model=MachineStatus)
def get_status() -> MachineStatus:
    return MachineStatus(**LATEST_STATE)


@router.post("/telemetry", response_model=MachineStatus)
def receive_telemetry(data: SensorData) -> MachineStatus:
    quality = evaluate_quality(
        temperature=data.temperature,
        diameter=data.diameter,
        speed=data.speed,
    )
    LATEST_STATE.update(
        {
            "temperature": data.temperature,
            "diameter": data.diameter,
            "speed": data.speed,
            "quality": quality,
        }
    )
    return MachineStatus(**LATEST_STATE)
