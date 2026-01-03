from ultralytics import YOLO

model = YOLO("yolov8n.pt")
model("data/sample.jpg", save=True)

print("Application ran successfully")
