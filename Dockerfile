FROM ultralytics/ultralytics:latest

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir geojson

COPY . .

CMD ["python", "src/infer.py"]
