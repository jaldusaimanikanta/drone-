import cv2
import os

# Folder where YOLOv8 saved the processed frames
input_folder = "yolo_outputs/results"

# Output video file name
output_path = "output_detected_video.mp4"

# Get list of processed frames
frames = sorted([f for f in os.listdir(input_folder) if f.endswith(".jpg")])

if not frames:
    print("[ERROR] No frames found.")
    exit()

# Load the first frame to get video dimensions
first_frame = cv2.imread(os.path.join(input_folder, frames[0]))
height, width, _ = first_frame.shape

# Define the codec and create a video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = 30  # Adjust if your original video had a different frame rate
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

# Write all frames into the video
for frame_name in frames:
    frame_path = os.path.join(input_folder, frame_name)
    frame = cv2.imread(frame_path)
    out.write(frame)

out.release()
print(f"[✅ DONE] Video saved as {output_path}")
