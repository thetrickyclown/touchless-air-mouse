# Beginner-Friendly GitHub Issues for Hacktoberfest

Copy and paste these into your GitHub repository as new issues.  
Each is labeled `good first issue` and `hacktoberfest`.

---

### Issue 1: Add Drag-and-Drop Gesture

**Title:** Add drag-and-drop support using a held pinch gesture

**Labels:** `good first issue`, `hacktoberfest`, `enhancement`

**Description:**

Currently the air-mouse supports single clicks. Many users would benefit from drag-and-drop functionality.

**Proposed Implementation:**
- When the user pinches thumb + index (left click threshold) and holds it for > 0.3 seconds, switch to drag mode.
- While in drag mode, call `pyautogui.mouseDown()` and continue tracking the index finger.
- Release (`pyautogui.mouseUp()`) when the fingers separate.
- Add a visual indicator in the camera feed (e.g., change text color or show "Dragging").

**Files to modify:**
- `core/gesture_mapper.py`
- `config.py` (add `DRAG_HOLD_TIME = 0.3`)
- `air_mouse.py` (optional status color)

**Acceptance Criteria:**
- User can drag files/windows by pinching and holding.
- No accidental drags during normal clicks.
- Status overlay clearly shows "Dragging".

---

### Issue 2: Add GUI Overlay for Toggle Status

**Title:** Create a simple status overlay / control panel

**Labels:** `good first issue`, `hacktoberfest`, `enhancement`

**Description:**

The current status is only text on the OpenCV window. A cleaner overlay or small control panel would improve usability.

**Ideas:**
- Show current mode with colored circles or icons.
- Add a small semi-transparent panel.
- Optional: keyboard shortcuts to temporarily disable tracking (`space` to pause).

**Acceptance Criteria:**
- Status is easier to read at a glance.
- Optional pause/resume functionality.
- Does not significantly impact FPS.

---

### Issue 3: Cross-Platform Testing & Fixes

**Title:** Verify and fix behavior on Windows, macOS, and Linux

**Labels:** `good first issue`, `hacktoberfest`, `bug`

**Description:**

PyAutoGUI and OpenCV can behave differently across operating systems (especially permissions and screen coordinates).

**Tasks:**
- Test on at least two platforms.
- Document any platform-specific setup steps in the README.
- Fix any issues with cursor mapping or failsafe on high-DPI displays.
- Check if `pyautogui.size()` correctly reports logical resolution.

**Acceptance Criteria:**
- README contains a "Platform Notes" section.
- Known issues are documented or fixed.

---

### Issue 4: Improve Smoothing with One Euro Filter

**Title:** Replace EMA with One Euro Filter for better smoothness vs latency

**Labels:** `good first issue`, `hacktoberfest`, `enhancement`

**Description:**

The current Exponential Moving Average works but can feel laggy or still jittery. The One Euro Filter is a popular choice for interactive systems because it adapts to speed.

**Resources:**
- https://gery.casiez.net/1euro/
- Reference Python implementations are widely available.

**Tasks:**
- Implement One Euro Filter in `gesture_mapper.py`.
- Add tunable parameters (`min_cutoff`, `beta`) to `config.py`.
- Keep the old EMA as a fallback option.

**Acceptance Criteria:**
- Cursor feels more responsive while remaining stable.
- Parameters are documented.

---

### Issue 5: Add Keyboard Shortcut to Toggle Tracking

**Title:** Add a hotkey to pause/resume hand tracking

**Labels:** `good first issue`, `hacktoberfest`, `enhancement`

**Description:**

Users sometimes need to quickly disable the air-mouse without quitting the program (e.g., to use the physical mouse).

**Proposed Implementation:**
- Listen for a key (e.g., `space` or `p`) in the main loop.
- When paused, ignore landmarks and show "PAUSED" on the overlay.
- Resume on the same key.

**Files to modify:**
- `air_mouse.py`

**Acceptance Criteria:**
- Tracking can be toggled without restarting.
- Clear visual feedback when paused.
- No accidental mouse movements while paused.

---

These issues are ready to be created on GitHub. They are designed so beginners can successfully contribute during Hacktoberfest.
