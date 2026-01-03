from ultralytics import YOLO
from gps import attach_gps
from geojson_export import export_geojson
import time

# Load model
model = YOLO("yolov8n.pt")

start_time = time.time()
results = model("data/sample.jpg", save=True)
end_time = time.time()

# Extract detections
detections = []
for r in results:
    for box in r.boxes:
        detections.append({
            "class": int(box.cls[0]),
            "confidence": float(box.conf[0])
        })

# Attach GPS
gps_detections = attach_gps(detections)

# Export GeoJSON
export_geojson(gps_detections)

# FPS metric
fps = 1 / (end_time - start_time)

print("Detections:", len(detections))
print("FPS:", round(fps, 2))
print("GeoJSON exported to outputs/detections.geojson")
