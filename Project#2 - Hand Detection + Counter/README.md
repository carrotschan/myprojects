# MediaPipe Hand Tracking & Finger Counting App

A real-time computer vision application that captures video feeds using **OpenCV** and tracks hand landmarks using Google's **MediaPipe Tasks Vision API**. It calculates finger positions, tracks distances between fingertips (like thumb and index), detects raised fingers via joint angle calculations, and draws dynamic bounding boxes and visual indicators around detected hands.

---

## Libraries Used

1. **OpenCV** (`cv2`) – For capturing video feeds, drawing shapes/text, and handling real-time image processing windows.
2. **MediaPipe** (`mediapipe`) – For robust hand landmark detection and tracking.
3. **Math** (`math`) – For mathematical calculations, including distance (`math.dist`) and angle computations (`math.atan2`, `math.degrees`) to determine whether fingers are raised.
4. **MediaPipe Tasks Python** (`mediapipe.tasks.python.python` & `vision`) – Utilizing the newer Task APIs (`HandLandmarkerOptions`, `BaseOptions`) for loading the hand tracking model.

---

## Prerequisites & Model Setup

This script requires a MediaPipe hand tracking model asset file to function properly:
* You need to download the **Hand Landmarker model file** (`hand_landmarker.task`) and place it in the same directory as your Python script.

---

## Installation

Install the required dependencies using pip:

```
cmd
pip install opencv-python mediapipe numpy

install opencv-python mediapipe numpy
```

## How to Run

Save your script as hand_tracker.py, ensure the hand_landmarker.task file is in the same folder, and execute the script from your terminal:
DOS

python hand_tracker.py


## Features & Logic

    * Multi-hand Support: Configured to track up to 4 hands simultaneously (num_hands=4) with high-confidence filtering (min_hand_detection_confidence = 0.8).

    * Distance Tracking: Calculates and visualizes the pixel distance between the index fingertip and thumb tip with a dynamic connecting line.

    * Finger State Detection: Measures angles between finger joints to accurately determine if individual fingers (Thumb, Index, Middle, Ring, Pinky) are raised.

    * Visual Bounding Boxes & UI: Automatically maps landmarks, creates custom colored bounding boxes per hand, and displays a live count of raised fingers.
