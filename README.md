# Touchless Air-Mouse & Gesture OS Control

A lightweight, beginner-friendly touchless mouse and OS controller that tracks your hand via webcam and maps finger landmarks to cursor actions. Perfect for Hacktoberfest contributions!

Built with **OpenCV**, **Google MediaPipe Hands**, and **PyAutoGUI**.

## Features

- Real-time hand tracking (21 landmarks)
- Smooth cursor movement using exponential moving average (reduces jitter)
- Left click: Pinch thumb + index finger
- Right click: Pinch thumb + middle finger
- Scroll mode: Hold index + middle fingers together and move vertically
- Safety fail-safe: Move mouse to any screen corner to instantly abort
- Modular, well-commented code with error handling

## Project Structure

```
touchless-air-mouse/
├── air_mouse.py              # Main launcher script
├── config.py                 # All tunable parameters
├── core/
│   ├── __init__.py
│   ├── hand_tracker.py       # MediaPipe + OpenCV landmark extraction
│   └── gesture_mapper.py     # Gesture detection & pyautogui actions
├── requirements.txt
├── README.md
└── CONTRIBUTING.md
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/touchless-air-mouse.git
   cd touchless-air-mouse
   ```

2. (Recommended) Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   Or manually:
   ```bash
   pip install opencv-python mediapipe pyautogui
   ```

## Usage

```bash
python air_mouse.py
```

- A window will open showing your webcam feed with hand landmarks.
- Move your **index fingertip** to control the mouse cursor.
- Pinch **thumb + index** for left click.
- Pinch **thumb + middle** for right click.
- Bring **index and middle fingertips** close together, then move up/down to scroll.
- Press `q` in the video window to quit.

### Safety Notes

- `pyautogui.FAILSAFE = True` is enabled by default.  
  **Quickly move the mouse to any corner of the screen** to immediately stop the script.
- Start with your hand in a neutral position. Adjust thresholds in `config.py` if clicks feel too sensitive.
- Works best with good lighting and a clear view of your hand.

## Configuration

Edit `config.py` to tune:

- Gesture distance thresholds
- Smoothing factor
- Click cooldown
- Scroll sensitivity
- Camera resolution

## Contributing

We welcome contributions, especially during Hacktoberfest!  
See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on adding new gestures, improving smoothing, or other enhancements.

## License

MIT License — feel free to use, modify, and distribute.

## Acknowledgments

- MediaPipe Hands by Google
- OpenCV
- PyAutoGUI
