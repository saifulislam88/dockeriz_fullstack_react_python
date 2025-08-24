FROM python:3.9-slim
WORKDIR /app
COPY consumer.py .
RUN pip install pika
CMD ["python", "consumer.py"]
