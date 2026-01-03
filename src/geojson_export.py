import geojson

def export_geojson(detections, output_path="outputs/detections.geojson"):
    features = []
    for d in detections:
        features.append(
            geojson.Feature(
                geometry=geojson.Point((d["longitude"], d["latitude"])),
                properties={
                    "class": d["class"],
                    "confidence": d["confidence"]
                }
            )
        )
    geojson.dump(geojson.FeatureCollection(features), open(output_path, "w"))