# OpenFilamentX MVP Build Guide

## Goal
Create a first working prototype that measures extrusion temperature, filament diameter, and speed.

## Suggested MVP steps
1. Assemble the extruder, heater, and motor control.
2. Attach temperature and diameter sensors.
3. Stream sensor output from ESP32 or Raspberry Pi.
4. Post telemetry to the FastAPI backend.
5. Visualize current state in the dashboard.
6. Run simple anomaly checks against a 1.75 mm target.

## Next milestones
- Add persistent storage
- Add calibration workflow
- Add control loop for automatic tuning
