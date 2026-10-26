#!/bin/bash
cd "$(dirname "$0")"

# Create venv if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate venv
source venv/bin/activate

# Install requirements if needed
if ! python -c "import mediapipe" 2>/dev/null; then
    echo "Installing dependencies..."
    pip install -r requirements.txt
fi

# Download model if missing (with SSL workaround)
if [ ! -f "hand_landmarker.task" ]; then
    echo "Downloading hand model..."
    curl -L -o hand_landmarker.task "https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task"
fi

# Run the air mouse
python air_mouse.py
