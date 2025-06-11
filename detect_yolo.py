from ultralytics import YOLO
import os

# Load the YOLOv8 Nano model (lightweight and fast)
model = YOLO("yolov8n.pt")  # you can also try yolov8s.pt for better accuracy

# Folder containing your extracted frames
input_folder = "frames"

# Folder to save detection results
output_folder = "yolo_outputs"
os.makedirs(output_folder, exist_ok=True)

# Run detection on each frame
for filename in sorted(os.listdir(input_folder)):
    if filename.endswith(".jpg"):
        frame_path = os.path.join(input_folder, filename)

        print(f"[INFO] Detecting objects in {filename}...")

        results = model(
            frame_path,
            save=True,
            save_txt=True,
            project=output_folder,
            name="results"
        )

print("[✅ DONE] YOLO detection complete. Check the 'yolo_outputs/results/' folder.")
