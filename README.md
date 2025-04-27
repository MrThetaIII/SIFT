# Multi-View Object Detection and Tracking Project

## Overview

This project provides three advanced computer vision scripts for object detection, tracking, and matching across different scenarios:

1. **SIFT Object-to-Object Matching** (`sift-o2o.ipynb`)
2. **SIFT Object-to-Video Tracking** (`sift-o2v.ipynb`)
3. **Stereo Video Object Tracking** (`sift-v2v.ipynb`)

## Prerequisites

### Python Dependencies

- OpenCV (`cv2`)
- NumPy
- MoviePy
- Ultralytics YOLO
- Supervision
- tkinter
- torch

### Installation

```bash
pip install opencv-python numpy moviepy ultralytics supervision torch tkinter
```

## Script Descriptions

### 1. SIFT Object-to-Object Matching (`sift-o2o.ipynb`)

- Matches a specific object image within a scene image
- Uses SIFT (Scale-Invariant Feature Transform) for feature detection
- Draws bounding box around matched object
- Visualizes feature matches

#### Object to Object Usage

```python
object_path = 'Object.jpg'
scene_path = 'Picture.jpg'
find_and_draw_object(object_path, scene_path)
```

### 2. SIFT Object-to-Video Tracking (`sift-o2v.ipynb`)

- Tracks an object's presence in a video
- Highlights object locations across video frames
- Preserves original video audio
- Supports multiple video codecs

#### Object to Video Usage

```python
video_path = 'video-o.mp4'
object_path = 'VObject.jpg'
output_path = 'output_video.mp4'
process_video(video_path, object_path, output_path)
```

### 3. Stereo Video Object Tracking (`sift-v2v.ipynb`)

- Multi-view object detection and tracking
- Uses YOLO for object detection
- SIFT for feature matching between views
- Provides depth estimation
- Interactive time selection

#### Video to Video Usage

```python
video1_path = "Rec-L.mp4"
video2_path = "Rec-R.mp4"
output_path = "stereo_output"
process_stereo_video(video1_path, video2_path, output_path, use_gui=True)
```

## Key Features

- SIFT-based feature matching
- YOLO object detection
- Multi-view tracking
- Interactive time selection
- Depth estimation
- Audio preservation

## Dependency Versions

- opencv-python: 4.10.0
- numpy: 1.24.3
- moviepy: 1.0.3
- ultralytics: 8.3.113
- supervision: 0.25.1
- torch: 2.4.1

## System Requirements

- Python 3.8+
- GPU recommended (CUDA-enabled)
- Minimum 16GB RAM
- OpenCV compiled with CUDA support (optional but recommended)
