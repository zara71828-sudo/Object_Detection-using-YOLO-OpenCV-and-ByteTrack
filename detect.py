from ultralytics import YOLO
import cv2
import os
import time

# ==========================
# Load YOLOv8 Model
# ==========================

print("=" * 55)
print("     AI OBJECT DETECTION & TRACKING SYSTEM")
print("=" * 55)
print("Developer : Zara Khan")
print("Model     : YOLOv8 Nano")
print("Tracker   : ByteTrack")
print("=" * 55)
print("\nLoading YOLOv8 model...")
model = YOLO("yolov8n.pt")
print("Model loaded successfully!\n")

# ==========================
# List Available Videos
# ==========================

video_folder = "videos"

if not os.path.exists(video_folder):
    print("Error: 'videos' folder not found.")
    exit()

videos = [file for file in os.listdir(video_folder) if file.endswith(".mp4")]

if len(videos) == 0:
    print("No MP4 videos found inside the videos folder.")
    exit()

print("========== Available Videos ==========\n")

for i, video in enumerate(videos, start=1):
    print(f"{i}. {video}")

print()

# ==========================
# User Selection
# ==========================

while True:
    try:
        choice = int(input("Select video number: "))

        if 1 <= choice <= len(videos):
            break

        print("Invalid choice. Try again.\n")

    except ValueError:
        print("Please enter a valid number.\n")

video_path = os.path.join(video_folder, videos[choice - 1])

print(f"\nSelected Video: {videos[choice-1]}")
print("Starting Object Detection & Tracking...\n")

# ==========================
# Open Video
# ==========================

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Unable to open the selected video.")
    exit()

# ==========================
# Video Properties
# ==========================

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

if total_frames <= 0:
    total_frames = 1

# ==========================
# Output Folder
# ==========================

output_folder = "outputs"
os.makedirs(output_folder, exist_ok=True)

output_path = os.path.join(
    output_folder,
    f"tracked_{os.path.splitext(videos[choice-1])[0]}.mp4"
)

# ==========================
# Video Writer
# ==========================

fourcc = cv2.VideoWriter_fourcc(*"mp4v")

out = cv2.VideoWriter(
    output_path,
    fourcc,
    fps,
    (width, height)
)

# ==========================
# Class Names
# ==========================

class_names = model.names

# ==========================
# FPS Calculation
# ==========================

prev_time = time.time()

# ==========================
# Processing Loop
# ==========================

frame_count = 0

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # ----------------------
    # YOLO Tracking
    # ----------------------

    results = model.track(
        frame,
        persist=True,
        tracker="bytetrack.yaml",
        verbose=False
    )

    # Object counters
    object_counter = {}

    # ----------------------
    # Draw Custom Boxes
    # ----------------------

    if results[0].boxes is not None:

        boxes = results[0].boxes

        for box in boxes:

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            cls = int(box.cls[0])
            conf = float(box.conf[0])

            # Tracking ID
            track_id = int(box.id[0]) if box.id is not None else 0

            class_name = class_names[cls]

            # Count objects
            object_counter[class_name] = object_counter.get(class_name, 0) + 1

            # Unique color from ID
            color = (
                (track_id * 37) % 255,
                (track_id * 17) % 255,
                (track_id * 29) % 255
            )

            # Draw box
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 3)

            # Label
            label = f"{class_name} #{track_id} ({conf:.2f})"

            cv2.putText(
                frame,
                label,
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                color,
                2
            )

    # ----------------------
    # FPS Display
    # ----------------------

    current_time = time.time()
    fps_display = 1 / (current_time - prev_time)
    prev_time = current_time

    cv2.putText(
        frame,
        f"FPS: {int(fps_display)}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    # ----------------------
    # Object Count Panel
    # ----------------------

    y_offset = 80

    for obj_name, count in object_counter.items():

        text = f"{obj_name}: {count}"

        cv2.putText(
            frame,
            text,
            (20, y_offset),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 255),
            2
        )

        y_offset += 30

    # ----------------------
    # Save Frame
    # ----------------------

    out.write(frame)

    frame_count += 1

    if frame_count % 10 == 0:
        percentage = (frame_count / total_frames) * 100
        print(f"Processing: {percentage:.1f}%")

# ==========================
# Cleanup
# ==========================

cap.release()
out.release()

report_path = os.path.join(output_folder, "report.txt")

with open(report_path, "w") as report:
    report.write("AI OBJECT DETECTION & TRACKING REPORT\n")
    report.write("=" * 45 + "\n\n")
    report.write(f"Input Video  : {videos[choice-1]}\n")
    report.write(f"Output Video : {output_path}\n")
    report.write(f"Frames Processed : {frame_count}\n")
    report.write(f"FPS              : {fps:.2f}\n")
    report.write(f"Model        : YOLOv8 Nano\n")
    report.write(f"Tracker      : ByteTrack\n")
    report.write("Status       : Completed Successfully\n")

print("\n" + "=" * 55)
print("        PROCESSING COMPLETED")
print("=" * 55)
print(f"Input Video   : {videos[choice-1]}")
print(f"Output Video  : {output_path}")
print(f"Frames Processed : {frame_count}")
print(f"Video FPS        : {fps:.2f}")
print(f"Report        : {report_path}")
print("Status        : SUCCESS")
print("=" * 55)