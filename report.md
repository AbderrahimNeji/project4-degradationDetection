# Experimental Results

A YOLOv8 model was used to detect road anomalies on a sample image.
The inference pipeline processes images, extracts detections, associates
each detection with simulated GPS coordinates, and exports the results as GeoJSON.

Performance metrics:

- FPS: measured during inference execution
- Detection results: qualitative evaluation of bounding boxes
- GeoJSON output: verified via map visualization

# Analysis and Interpretation

The system demonstrates a complete pipeline from detection to geolocation
and visualization. GPS coordinates were simulated due to the absence of
real GPS metadata, which is acceptable for a proof-of-concept implementation.

The map dashboard allows spatial inspection of detected anomalies.
Limitations include the lack of task-specific training data and real GPS
synchronization. Future work includes training on annotated datasets,
video-based processing, and accurate geolocation error measurement.
