import json
import psycopg2

with open("data/raw/yolo_detections.json") as f:
    data = json.load(f)

conn = psycopg2.connect(
    host="localhost",
    dbname="telegram",
    user="postgres",
    password="yourpassword"
)
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS raw.telegram_image_detections (detection_data jsonb);")
cur.execute("INSERT INTO raw.telegram_image_detections (detection_data) VALUES (%s)", [json.dumps(data)])
conn.commit()
cur.close()
conn.close()
print(" Loaded detections to PostgreSQL")
