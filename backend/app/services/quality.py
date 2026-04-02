def evaluate_quality(temperature: float, diameter: float, speed: float) -> str:
    diameter_ok = 1.70 <= diameter <= 1.80
    temp_ok = 190 <= temperature <= 240
    speed_ok = 1 <= speed <= 20

    if diameter_ok and temp_ok and speed_ok:
        return "good"
    if (1.65 <= diameter <= 1.85) and (180 <= temperature <= 250):
        return "warning"
    return "alert"
