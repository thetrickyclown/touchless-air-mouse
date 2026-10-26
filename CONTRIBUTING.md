# Contributing to Touchless Air-Mouse & Gesture OS Control

Thank you for your interest in contributing! This project is designed to be beginner-friendly and is open for Hacktoberfest contributions.

## How to Contribute

1. Fork the repository.
2. Create a new branch for your feature or fix:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Make your changes.
4. Test thoroughly (especially on different lighting conditions and screen resolutions).
5. Commit with a clear message:
   ```bash
   git commit -m "Add drag-and-drop gesture support"
   ```
6. Push to your fork and open a Pull Request.

## Adding a New OS Gesture

Here’s a step-by-step guide to add a new gesture (e.g., drag-and-drop or volume control):

1. **Define the gesture logic** in `core/gesture_mapper.py`:
   - Add a new distance or angle calculation using landmarks.
   - Example landmarks: 4 (thumb), 8 (index), 12 (middle), 16 (ring), 20 (pinky).

2. **Add configuration parameters** in `config.py`:
   ```python
   DRAG_THRESHOLD = 0.05
   ```

3. **Implement the action** using `pyautogui`:
   ```python
   pyautogui.mouseDown()
   # ... later
   pyautogui.mouseUp()
   ```

4. **Update the status message** returned by `process_gestures()` so the overlay shows the new state.

5. **Document the gesture** in the README under Features and Usage.

6. **Add tests or manual testing notes** in your PR description.

## Improving the Smoothing Algorithm

The current implementation uses a simple Exponential Moving Average (EMA) in `gesture_mapper.py` → `smooth_move()`.

Ideas for improvement:
- Adaptive smoothing based on movement speed
- One Euro Filter for better latency/smoothness trade-off
- Kalman filter
- Separate smoothing factors for X and Y

When improving smoothing:
- Keep the method signature the same if possible.
- Add the new parameters to `config.py`.
- Include before/after comparison notes in your PR.

## Code Style

- Use clear, descriptive variable names.
- Add comments for non-obvious logic (especially landmark indices).
- Handle the case where no hand is detected.
- Keep functions focused and modular.

## Labels

Please use the following labels on issues and PRs when applicable:
- `good first issue`
- `hacktoberfest`
- `enhancement`
- `bug`

## Questions?

Open an issue or start a discussion. We’re happy to help beginners get started!

Happy coding and happy Hacktoberfest!
