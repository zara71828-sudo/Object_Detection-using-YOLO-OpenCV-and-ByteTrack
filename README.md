# AI Object Detection & Tracking System

A real-time **Object Detection and Multi-Object Tracking** system developed using **YOLOv8**, **OpenCV**, and **ByteTrack**. The application detects multiple objects in videos, assigns unique tracking IDs, displays confidence scores, calculates FPS, counts detected objects, and saves the processed output video.


---

## Features

- 🎥 Multiple video selection
- 🚀 Real-time object detection using YOLOv8
- 🔄 Multi-object tracking with ByteTrack
- 🆔 Unique tracking ID for each detected object
- 📦 Custom colored bounding boxes
- 📊 Live object counting
- ⚡ FPS (Frames Per Second) display
- 🎯 Confidence score for each detection
- 💾 Automatic output video generation
- 📄 Automatic report generation
- 🖥️ Professional console interface
- 🛡️ Error handling for invalid videos and folders

---

## Technologies Used

- Python 3
- YOLOv8 (Ultralytics)
- OpenCV
- ByteTrack
- NumPy

---

## Project Structure

```
CodeAlpha_Object_Detection/
│
├── detect.py
├── requirements.txt
├── README.md
├── .gitignore
├── yolov8n.pt
│
├── videos/
│   ├── sample.mp4
│   ├── sample2.mp4
│
└── outputs/
    ├── tracked_sample.mp4
    ├── tracked_sample2.mp4
    └── report.txt
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/zara71828-sudo/Object_Detection.git
```

```bash
cd Object_Detection
```

---

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Project

Execute:

```bash
python detect.py
```

The program will display all available videos.

Example:

```
========== Available Videos ==========

1. sample.mp4
2. sample2.mp4

Select video number:
```

Choose a video number and the detection process will begin automatically.

---

## Output

The application generates:

- Processed video with object detection and tracking
- Bounding boxes
- Tracking IDs
- Confidence scores
- FPS counter
- Object count panel
- Processing report

All output files are saved inside the **outputs/** folder.

Example:

```
outputs/
│
├── tracked_sample.mp4
├── tracked_sample2.mp4
└── report.txt
```

---

## Sample Report

```
AI OBJECT DETECTION & TRACKING REPORT

Input Video  : sample.mp4
Output Video : outputs/tracked_sample.mp4

Frames Processed : 625

Model : YOLOv8 Nano
Tracker : ByteTrack

Status : Completed Successfully
```

---

## Detection Features

The system performs:

- Person Detection
- Car Detection
- Bus Detection
- Truck Detection
- Motorcycle Detection
- Bicycle Detection
- Animal Detection
- Any object supported by the YOLOv8 COCO dataset

---

## Workflow

1. Load YOLOv8 model
2. Display available videos
3. Select a video
4. Read video frames
5. Detect objects
6. Track objects using ByteTrack
7. Draw custom bounding boxes
8. Display tracking IDs
9. Count detected objects
10. Display FPS
11. Save processed video
12. Generate report

---

## Key Features

### Object Detection

Detects multiple objects present in the video.

### Object Tracking

Assigns a unique tracking ID to each detected object and keeps track of it across frames.

Example:

```
Person #3
Car #5
Truck #2
```

### FPS Monitoring

Displays the real-time processing speed.

Example:

```
FPS: 31
```

### Object Counter

Displays the number of detected objects.

Example:

```
Person : 4
Car : 7
Truck : 1
```

---

## Future Improvements

- Live webcam detection
- Custom-trained YOLO models
- Vehicle counting
- Speed estimation
- Traffic analytics
- Line crossing detection
- Face detection
- GUI interface using Streamlit or PyQt
- Export detection statistics to CSV

---

## Learning Outcomes

This project helped me gain practical experience in:

- Computer Vision
- Deep Learning
- Object Detection
- Multi-Object Tracking
- YOLOv8
- OpenCV
- Video Processing
- Artificial Intelligence
- Python Programming

---

## Developer

**Zara Khan**

BS Computer Science  
FAST National University of Computer and Emerging Sciences (FAST-NUCES), Peshawar

GitHub: https://github.com/zara71828-sudo

LinkedIn: www.linkedin.com/in/zara-khan-393848399

---

## Acknowledgements

- Ultralytics YOLOv8
- OpenCV
- ByteTrack
- Python Community

---

## License

This project is created for educational and internship purposes.

---

### If you found this project helpful, please consider giving it a star on GitHub!
