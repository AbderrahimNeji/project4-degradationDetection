import random

def attach_gps(detections, base_lat=48.8566, base_lon=2.3522):
    """
    Attach simulated GPS coordinates to detections.
    """
    gps_detections = []
    for det in detections:
        gps_detections.append({
            "class": det["class"],
            "confidence": det["confidence"],
            "latitude": base_lat + random.uniform(-0.0005, 0.0005),
            "longitude": base_lon + random.uniform(-0.0005, 0.0005)
        })
    return gps_detections
