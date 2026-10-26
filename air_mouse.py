"""
Touchless Air-Mouse & Gesture OS Control
Main launcher script.

Tracks hand movement via webcam and maps finger landmarks to mouse cursor actions
using OpenCV, MediaPipe Hands, and PyAutoGUI.

Usage:
    python air_mouse.py

Controls:
    - Move index finger to control cursor
    - Pinch thumb + index → Left Click
    - Pinch thumb + middle → Right Click
    - Hold index + middle together and move vertically → Scroll
    - Press 'q' to quit
"""

import cv2
import sys
from core.hand_tracker import HandTracker
from core.gesture_mapper import GestureMapper
from config import CAMERA_INDEX, FRAME_WIDTH, FRAME_HEIGHT

def main():
    print("Starting Touchless Air-Mouse...")
    print("Move mouse to any corner of the screen to emergency stop (FAILSAFE).")
    print("Press 'q' in the video window to quit.\n")

    # Initialize components
    tracker = HandTracker()
    mapper = GestureMapper()

    # Open webcam
    cap = cv2.VideoCapture(CAMERA_INDEX)
    if not cap.isOpened():
        print("ERROR: Could not open webcam. Check CAMERA_INDEX in config.py")
        sys.exit(1)

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)

    try:
        while True:
            success, frame = cap.read()
            if not success:
                print("WARNING: Failed to read frame from camera.")
                continue

            # Process hand landmarks
            frame, landmarks = tracker.process_frame(frame)

            # Map gestures to OS actions
            status = mapper.process_gestures(landmarks)

            # Overlay status text on the frame
            cv2.putText(
                frame,
                f"Status: {status}",
                (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                2
            )
            cv2.putText(
                frame,
                "Press 'q' to quit",
                (10, FRAME_HEIGHT - 20),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (255, 255, 255),
                1
            )

            # Show the camera feed
            cv2.imshow("Touchless Air-Mouse", frame)

            # Exit on 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except KeyboardInterrupt:
        print("\nInterrupted by user.")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        # Cleanup
        cap.release()
        cv2.destroyAllWindows()
        tracker.close()
        print("Air-Mouse stopped. Resources released.")

if __name__ == "__main__":
    main()
