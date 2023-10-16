# Real-time Face Detection and Head Movement Control

This Python script uses MediaPipe Face Detection to track your facial movements in real-time and control keyboard inputs accordingly. It simulates keypresses for left and right movements and jumping based on your facial orientation.
This script was made to provide controls for [Asphalt 8](https://www.gameloft.com/game/asphalt-8), but can be adapted to any other medium as it simulates key presses for the focused window, and not inherently linked to the game's process.

### Controls
* **Lean head left**: presses `a`.
* **Lean head right**: presses `d`.
* **lean head down**: presses `Space`. 



## Prerequisites

Before running this code, make sure you have the following installed:
- Python 3
- OpenCV (cv2)
- MediaPipe
- Pynput

You can install the required libraries using pip:

```bash
pip install opencv-python mediapipe pynput
```

## How to Use
1. Clone this repository or download the script.
2. Connect a webcam to your computer.
3. Run the script using Python:
```bash
python vision.py
```
4. The webcam will start, and it will track your facial movements.
5. As you lean your face to the left, it will simulate a `d` keypress, moving to the right simulates an `a` keypress, and lowering your head simulates the `space` keypress.
6. To exit the script, press `q` in the webcam window.

## Configuration
You can adjust the following parameters in the script:

* `face_detection_threshold`: Adjust the confidence threshold for face detection.
* `lean_threshold`: Change the threshold for leaning detection.
* `head_lower_threshold`: Adjust the threshold for detecting the head moving lower.

You can also extend the controls t fit your needs.

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/Issaminu/face-motion-input/blob/main/LICENSE) file for details.

## Acknowledgments
This code uses [MediaPipe](https://github.com/google/mediapipe) for face detection and [Pynput](https://github.com/moses-palmer/pynput) for keyboard control.

Feel free to modify and improve this code for your specific applications. If you encounter any issues or have suggestions, please create an issue in this repository.

