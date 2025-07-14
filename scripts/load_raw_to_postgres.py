import os
import json
import psycopg2
from psycopg2.extras import execute_values

# Connect to your PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    dbname="your_database_name",
    user="your_postgres_user",
    password="your_postgres_password",
    port=5432
)
cur = conn.cursor()

# Create raw schema if not exists
cur.execute("CREATE SCHEMA IF NOT EXISTS raw;")
conn.commit()

# Create table raw.telegram_messages (adjust columns as needed)
cur.execute("""
CREATE TABLE IF NOT EXISTS raw.telegram_messages (
    id SERIAL PRIMARY KEY,
    message_id INT,
    channel VARCHAR,
    message TEXT,
    date TIMESTAMP,
    media JSONB
);
""")
conn.commit()

# Folder containing your raw JSON files
data_folder = 'data/raw/telegram_messages/2025-07-13/'

for filename in os.listdir(data_folder):
    if filename.endswith(".json"):
        channel_name = filename.replace('.json', '')
        file_path = os.path.join(data_folder, filename)
        with open(file_path, 'r', encoding='utf-8') as f:
            messages = json.load(f)
            records = []
            for msg in messages:
                records.append((
                    msg.get('id'),
                    channel_name,
                    msg.get('message'),
                    msg.get('date'),
                    json.dumps(msg.get('media'))
                ))

            sql = """
            INSERT INTO raw.telegram_messages (message_id, channel, message, date, media)
            VALUES %s
            ON CONFLICT (message_id) DO NOTHING;
            """
            execute_values(cur, sql, records)
            conn.commit()

cur.close()
conn.close()
