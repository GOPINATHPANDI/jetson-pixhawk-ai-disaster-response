# System Architecture

## Companion Computer (Jetson Nano)
- Runs AI inference
- Processes camera and LiDAR data
- Publishes ROS topics
- Sends MAVLink telemetry to Pixhawk

## Flight Controller (Pixhawk)
- Handles stabilization and control
- Receives telemetry and offboard commands
- Executes avoidance maneuvers

## Communication
- ROS for internal data flow
- MAVLink for Jetson–Pixhawk communication
