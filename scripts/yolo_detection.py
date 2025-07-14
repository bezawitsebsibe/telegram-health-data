from ultralytics import YOLO
import os
import json
from datetime import datetime

# Load YOLOv8 model (pretrained)
model = YOLO("yolov8n.pt")  # nano version = fast and small

# Path to image folder
image_folder = "data/raw/images/lobelia4cosmetics"
output_path = "data/raw/yolo_detections.json"

results_list = []

for image_name in os.listdir(image_folder):
    if image_name.endswith((".jpg", ".png")):
        image_path = os.path.join(image_folder, image_name)
        results = model(image_path)

        for r in results:
            for box in r.boxes:
                detection = {
                    "image": image_name,
                    "class": model.names[int(box.cls)],
                    "confidence": float(box.conf),
                    "timestamp": datetime.now().isoformat()
                }
                results_list.append(detection)

# Save all detections to JSON
with open(output_path, "w") as f:
    json.dump(results_list, f, indent=4)

print(f"✅ Detection results saved to {output_path}")
