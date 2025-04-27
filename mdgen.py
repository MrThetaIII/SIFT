import os
import html
def get_dependency_versions():
    """Dynamically get installed package versions"""
    dependencies = [
        'opencv-python', 'numpy', 'moviepy', 
        'ultralytics', 'supervision', 'torch'
    ]
    versions = []
    for dep in dependencies:
        try:
            import importlib.metadata
            version = importlib.metadata.version(dep)
            # Use html.escape to handle any special characters
            versions.append(f"- {html.escape(dep)}: {html.escape(version)}")
        except:
            versions.append(f"- {html.escape(dep)}: Not installed")
    return "\n".join(versions)

def escape_special_chars(text):
    """
    Escape special markdown characters
    """
    # List of special characters to escape
    special_chars = {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#39;',
        '`': '&#96;',
        '*': '&#42;',
        '_': '&#95;',
        '{': '&#123;',
        '}': '&#125;',
        '[': '&#91;',
        ']': '&#93;',
        '(': '&#40;',
        ')': '&#41;',
        '#': '&#35;',
        '+': '&#43;',
        '-': '&#45;',
        '.': '&#46;',
        '!': '&#33;'
    }
    
    # Replace special characters
    for char, replacement in special_chars.items():
        text = text.replace(char, replacement)
    
    return text

def generate_readme():
    readme_content = f"""# Multi-View Object Detection and Tracking Project

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
&#96;&#96;&#96;bash
pip install opencv-python numpy moviepy ultralytics supervision torch tkinter
&#96;&#96;&#96;

## Script Descriptions

### 1. SIFT Object-to-Object Matching (`sift-o2o.ipynb`)
- Matches a specific object image within a scene image
- Uses SIFT (Scale-Invariant Feature Transform) for feature detection
- Draws bounding box around matched object
- Visualizes feature matches

#### Usage
&#96;&#96;&#96;python
object_path = &#39;Object.jpg&#39;
scene_path = &#39;Picture.jpg&#39;
find_and_draw_object(object_path, scene_path)
&#96;&#96;&#96;

### 2. SIFT Object-to-Video Tracking (`sift-o2v.ipynb`)
- Tracks an object&#39;s presence in a video
- Highlights object locations across video frames
- Preserves original video audio
- Supports multiple video codecs

#### Usage
&#96;&#96;&#96;python
video_path = &#39;video-o.mp4&#39;
object_path = &#39;VObject.jpg&#39;
output_path = &#39;output_video.mp4&#39;
process_video(video_path, object_path, output_path)
&#96;&#96;&#96;

### 3. Stereo Video Object Tracking (`sift-v2v.ipynb`)
- Multi-view object detection and tracking
- Uses YOLO for object detection
- SIFT for feature matching between views
- Provides depth estimation
- Interactive time selection

#### Usage
&#96;&#96;&#96;python
video1_path = &#34;Rec-L.mp4&#34;
video2_path = &#34;Rec-R.mp4&#34;
output_path = &#34;stereo_output&#34;
process_stereo_video(video1_path, video2_path, output_path, use_gui=True)
&#96;&#96;&#96;

## Key Features
- SIFT-based feature matching
- YOLO object detection
- Multi-view tracking
- Interactive time selection
- Depth estimation
- Audio preservation

## Performance Considerations
- Requires significant computational resources
- Performance varies with input video/image quality
- Recommended for machines with good GPU support

## Troubleshooting
- Ensure all dependencies are correctly installed
- Check input file paths
- Verify input video/image formats
- Update OpenCV and YOLO model versions if encountering compatibility issues

## Limitations
- Sensitive to image/video quality
- Performance depends on feature distinctiveness
- May struggle with highly similar or occluded objects

## Dependency Versions
{get_dependency_versions()}

## System Requirements
- Python 3.8+
- GPU recommended (CUDA-enabled)
- Minimum 16GB RAM
- OpenCV compiled with CUDA support (optional but recommended)

## Recommended Hardware
- Processor: Intel Core i7/i9 or AMD Ryzen 7/9
- GPU: NVIDIA RTX 3060 or higher
- RAM: 32GB or more

## Potential Applications
- Computer Vision Research
- Object Tracking
- Autonomous Systems
- Surveillance Systems
- Augmented Reality

## Future Improvements
- Advanced feature matching algorithms
- More robust depth estimation
- Support for more object classes
- Enhanced performance optimization
- Machine learning model fine-tuning

## Troubleshooting Common Issues
1. **Dependency Conflicts**
   - Use virtual environments
   - Ensure compatible library versions
   
2. **Performance Bottlenecks**
   - Use GPU acceleration
   - Optimize input video resolution
   
3. **Feature Matching Challenges**
   - Preprocess images
   - Adjust matching thresholds
   - Use alternative feature detectors

## License
[Specify your project&#39;s license here]

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

### Contribution Guidelines
- Follow PEP 8 style guide
- Write clear, concise code
- Include docstrings and comments
- Add/update tests for new features

## Citation
If you use this project in academic research, please cite:
&#96;&#96;&#96;
&#64;misc{{MultiViewObjectTracking,
  title={{Multi-View Object Detection and Tracking}},
  author={{Your Name}},
  year={{2024}}
}}
&#96;&#96;&#96;

## Acknowledgments
- OpenCV Community
- Ultralytics YOLO Team
- Python Scientific Computing Community
"""
    # Write to README.md
    with open('README.md', 'w', encoding='utf-8') as f:
        # Optionally, you can use escape_special_chars if needed
        f.write(readme_content)

    print("README.md generated successfully!")

    

def main():
    generate_readme()

if __name__ == "__main__":
    main()