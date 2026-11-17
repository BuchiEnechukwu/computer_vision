# Real-Time Multi-Colour Detection Using OpenCV

## Project Overview

This project explores computer vision techniques for detecting and identifying multiple colours in real time using Python and OpenCV.

The application captures live video from a webcam, processes each frame in the HSV (Hue, Saturation, Value) colour space, and identifies regions corresponding to predefined colours. Detected regions are highlighted with bounding boxes and labelled with their respective colour names.

The project currently supports five colours: **red, yellow, blue, green, and orange**.

## Demonstration

The screenshot below demonstrates real-time colour
detection using a webcam. The application identifies
matching colour regions and highlights them with
labelled bounding boxes.

![Real-time multi-colour detection](images/color_detection_demo.png)

## Features

- Real-time video capture using a webcam.
- Simultaneous detection of five predefined colours.
- Conversion of video frames from BGR to HSV colour space.
- Dynamic HSV threshold generation for colour identification.
- Handling of hue wrap-around for colours such as red.
- Contour detection and bounding boxes around matching colour regions.
- Colour labels displayed on the live video feed.
- Filtering of small colour regions to reduce noise.

## Technologies Used

- **Python** – Core programming language.
- **OpenCV** – Webcam capture, image processing, colour masking, and contour detection.
- **NumPy** – Array manipulation and mask processing.
- **Pillow** – Included in the project dependencies.

## Project Structure

```text
computer_vision/
├── maincolors.py
├── util.py
├── requirements.txt
└── .gitignore
```

**maincolors.py:** The main application responsible for webcam capture, colour detection, contour identification, and visualisation.

**util.py:** Contains the `get_limits()` function for dynamically calculating HSV ranges from BGR colour values.

**requirements.txt:** Lists the Python libraries required by the project.

## How It Works

The colour detection process follows six main steps:

1. **Frame capture:** OpenCV captures video frames from the connected webcam.
2. **Colour-space conversion:** Each frame is converted from BGR to HSV for colour-based segmentation.
3. **HSV thresholding:** The `get_limits()` function calculates the appropriate HSV ranges for each target colour.
4. **Mask generation:** Binary masks isolate pixels that fall within the specified colour ranges.
5. **Contour detection:** OpenCV identifies the boundaries of matching colour regions. Regions with contour areas smaller than 500 pixels² are ignored.
6. **Visualisation:** Bounding boxes and colour labels are drawn around detected regions on the live video feed.

For red, the implementation accounts for the circular nature of HSV hue values by combining two ranges near the lower and upper boundaries of the hue scale.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/BuchiEnechukwu/computer_vision.git
cd computer_vision
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

Activate it on macOS/Linux:

```bash
source .venv/bin/activate
```

### 3. Install the required libraries

```bash
python -m pip install -r requirements.txt
```

### 4. Run the application

```bash
python maincolors.py
```

The webcam should open and begin detecting colours in real time.

Press **Q** while the webcam window is active to terminate the application.

## Current Limitations

- Detection accuracy depends on lighting conditions, shadows, and camera quality.
- Objects with similar colours to the background may also be detected.
- HSV threshold ranges are based on predefined tolerances rather than adaptive calibration.
- The program identifies colour regions rather than recognising specific object categories.
- Multiple nearby regions of the same colour may be detected as one region.

## Future Improvements

- Implement morphological filtering to reduce noise in colour masks.
- Introduce interactive HSV threshold calibration.
- Track detected colour regions across consecutive video frames.
- Incorporate object detection models to distinguish objects beyond their colours.
- Develop a user interface for selecting target colours dynamically.




