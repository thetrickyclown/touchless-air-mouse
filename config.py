"""
Configuration parameters for Touchless Air-Mouse & Gesture OS Control.
Centralized settings for easy tuning by contributors.
"""

import pyautogui

# Screen resolution (auto-detected)
SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()

# Camera settings
CAMERA_INDEX = 0
FRAME_WIDTH = 640
FRAME_HEIGHT = 480

# Gesture distance thresholds (Euclidean distance in normalized landmark space, 0.0-1.0)
# Lower values = stricter / closer fingers required
LEFT_CLICK_THRESHOLD = 0.055   # Thumb tip (4) to Index tip (8) — slightly more forgiving
RIGHT_CLICK_THRESHOLD = 0.050  # Thumb tip (4) to Middle tip (12)
SCROLL_FINGERS_THRESHOLD = 0.07  # Index tip (8) to Middle tip (12) to enter scroll mode

# Desktop switching (horizontal swipe while fingers are together)
DESKTOP_SWIPE_THRESHOLD = 0.04   # Minimum horizontal movement to switch desktops
DESKTOP_SWIPE_COOLDOWN = 0.6     # Seconds between desktop switches

# Smoothing for cursor movement (Exponential Moving Average)
# Higher value = smoother but more lag. Recommended: 0.5 - 0.8
SMOOTHING_FACTOR = 0.65

# Click cooldown in seconds to prevent rapid-fire clicks
CLICK_COOLDOWN = 0.4

# Scroll sensitivity (pixels per frame of vertical movement while in scroll mode)
SCROLL_SENSITIVITY = 15

# Safety
# Move mouse to corner to abort (pyautogui built-in)
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.01  # Small pause between actions for stability

# Horizontal inversion
# Set to False if moving your hand left moves the cursor right
INVERT_X = True
