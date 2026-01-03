# Project 4 – Degradation Detection (Computer Vision)

## Project Description

This project focuses on detecting and classifying road and infrastructure degradation
such as potholes, cracks, and faded road markings using computer vision techniques.
A YOLO-based object detection model is used to analyze images and demonstrate the
feasibility of automated road condition analysis.

## Setup

The project is implemented in Python and containerized using Docker to ensure easy
setup and reproducibility.

## Usage (Docker)

### Build the Docker image

```bash
docker build -t degradation-detection .
```

## Additional Features

- Simulated GPS association for detections
- GeoJSON export of detected anomalies
- Interactive map dashboard using Leaflet
- Performance metrics (FPS)
