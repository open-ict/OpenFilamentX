def detect_anomaly(diameter: float, target: float = 1.75, tolerance: float = 0.05) -> str:
    deviation = abs(diameter - target)
    if deviation <= tolerance:
        return "OK"
    if deviation <= tolerance * 2:
        return "WARNING"
    return "ALERT"


if __name__ == "__main__":
    for value in [1.74, 1.82, 1.90]:
        print(value, detect_anomaly(value))
