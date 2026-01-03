FROM ultralytics/ultralytics:latest

WORKDIR /app

COPY . .

CMD ["python", "src/infer.py"]
