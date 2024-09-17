# Car Distance and Visibility Detector

This repository contains a Python application that uses YOLOv8 to detect a car in an image and checks whether the car is properly captured with full body visible or some parts are missing. The script analyzes the distance of the car from the camera and determines whether the car is too close or too far.

## Features

- **Car Detection**: Uses the YOLOv8 model to detect cars in an image.
- **Camera Distance Check**: Calculates the proportion of the image occupied by the car to check if the camera is too close or too far.
- **Border Check**: Verifies if the car is fully visible within the image borders to ensure the capture is valid.
- **Real-time Feedback**: Provides feedback on whether the whole car is visible and whether the camera distance is appropriate.

## Requirements

- Python 3.x
- ultralytics (for YOLOv8)
- PIL (Python Imaging Library)

## Setup and Usage

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/car-distance-and-visibility-detector.git
cd car-distance-and-visibility-detector
```

2. Install Required Packages
You can install the required dependencies by running:

```bash
pip install -r requirements.txt
```

3. Add Your Image

```python
image_path = "/path/to/your/image.jpg"  # Update this path
```

4. Run the Script
```bash
python car_distance_and_visibility.py
```
The script will:

Detect the car in the provided image.
Check if the car is fully visible within the frame.
Evaluate the camera distance and provide feedback.

**Example Output:**

```bash
---
Coordinates: [21, 20, 622, 308]
Probability: 0.95
---
Car distance is optimal.
Car is captured properly. Not touching border.
```
