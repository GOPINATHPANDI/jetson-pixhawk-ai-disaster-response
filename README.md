# AI-Based Disaster Response Drone System

## Overview
This project implements an AI-powered drone system for disaster response using Jetson Nano as a companion computer and Pixhawk as the flight controller.

The system performs:
- Real-time object detection and counting
- Live video processing
- 2D mapping using RP-LiDAR
- Obstacle avoidance
- MAVLink communication with Pixhawk

---

## System Architecture
Camera → Jetson Nano → AI Detection → ROS  
Jetson Nano → MAVLink → Pixhawk  
RP-LiDAR → Jetson Nano → SLAM → Obstacle Avoidance

---

## Hardware Used
- Jetson Nano (Ubuntu 18.04)
- Pixhawk Orange
- RP-LiDAR
- USB / CSI Camera

---

## Software Stack
- Ubuntu 18.04
- ROS Melodic
- MAVROS / pymavlink
- OpenCV
- TensorRT / ONNX Runtime
- rplidar_ros
- gmapping

---

## Features
- Object detection and per-class counting
- Telemetry transmission to Pixhawk
- Live annotated video
- 2D SLAM mapping
- Reactive obstacle avoidance

---

## Model Weights
Trained model weights are not uploaded due to intellectual property and competition constraints.

---

## How to Run (High Level)
1. Start MAVROS
2. Start LiDAR node
3. Start SLAM
4. Run AI detection node

---

## My Contribution
- System architecture design
- AI inference deployment on Jetson Nano
- MAVLink telemetry integration
- LiDAR mapping and obstacle avoidance

---

## Results
Screenshots and logs are available in the results folder.
