import cv2
import os

# Create output folder (if it doesn't exist)
os.makedirs("frames", exist_ok=True)

# Path to the video file
video_path = "video.mp4"

# Open the video
cap = cv2.VideoCapture(video_path)

# Check if video opened successfully
if not cap.isOpened():
    print("[ERROR] Could not open video. Check if 'video.mp4' exists in the folder.")
    exit()

print("[INFO] Video opened successfully.")

# Frame counter
frame_num = 0

# Read frames in a loop
while True:
    success, frame = cap.read()

    if not success:
        print("[INFO] No more frames to read or error occurred.")
        break

    # Save current frame as an image
    filename = f"frames/frame_{frame_num:04d}.jpg"
    cv2.imwrite(filename, frame)

    print(f"[INFO] Saved {filename}")
    frame_num += 1

# Release the video object
cap.release()
print("[DONE] Frame extraction complete.")
