FROM python:3.9-slim

WORKDIR /app
COPY ./app.py .

RUN pip install --no-cache-dir flask psycopg2-binary pika

CMD ["python", "app.py"]

