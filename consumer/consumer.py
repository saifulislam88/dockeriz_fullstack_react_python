import pika
import json
import time

def connect_to_rabbitmq(retries=10, delay=5):
    for attempt in range(1, retries + 1):
        try:
            print(f"🔄 Attempting to connect to RabbitMQ... ({attempt}/{retries})")
            credentials = pika.PlainCredentials('myuser', 'mypass')
            connection = pika.BlockingConnection(pika.ConnectionParameters(
                host='rabbitmq',
                port=5672,
                credentials=credentials
            ))
            print("✅ Connected to RabbitMQ")
            return connection
        except pika.exceptions.AMQPConnectionError:
            print("❌ RabbitMQ not ready, retrying...")
            time.sleep(delay)
    raise Exception("🚨 Could not connect to RabbitMQ after multiple attempts.")

def callback(ch, method, properties, body):
    try:
        data = json.loads(body)
        print("📥 Consumed message from queue:", data)
        # Optional: perform action or send email
    except json.JSONDecodeError:
        print("❌ Error decoding JSON message")

def main():
    connection = connect_to_rabbitmq()
    channel = connection.channel()
    channel.queue_declare(queue='student_queue', durable=True)
    channel.basic_consume(queue='student_queue', on_message_callback=callback, auto_ack=True)

    print("🎧 Waiting for messages. To exit press CTRL+C")
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        print("🛑 Stopped manually")
    finally:
        connection.close()

if __name__ == "__main__":
    main()

