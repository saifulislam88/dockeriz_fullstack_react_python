from flask import Flask, request, jsonify
import psycopg2
import pika
import json

app = Flask(__name__)

# PostgreSQL connection
conn = psycopg2.connect(
    dbname='appdb', user='user', password='pass', host='postgres'
)
cur = conn.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id SERIAL PRIMARY KEY,
        name TEXT,
        email TEXT,
        batch TEXT
    )
""")
conn.commit()

@app.route('/api/submit', methods=['POST'])
def submit():
    try:
        data = request.get_json()

        # Save to DB
        cur.execute(
            "INSERT INTO students (name, email, batch) VALUES (%s, %s, %s)",
            (data['name'], data['email'], data['batch'])
        )
        conn.commit()

        # Send to RabbitMQ
        credentials = pika.PlainCredentials('myuser', 'mypass')
        connection = pika.BlockingConnection(pika.ConnectionParameters(
            host='rabbitmq', credentials=credentials
        ))
        channel = connection.channel()
        channel.queue_declare(queue='student_queue', durable=True)

        channel.basic_publish(
            exchange='',
            routing_key='student_queue',
            body=json.dumps(data)  # ✅ Proper JSON format
        )
        connection.close()

        return jsonify({"message": "Data stored and queued."}), 200

    except Exception as e:
        print("🔥 Error:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

