# Visual-Calc
A gesture-controlled virtual calculator using Python, OpenCV, and Mediapipe. Use your index finger and tap gestures via webcam to perform touchless arithmetic operations in real time. Lightweight, intuitive, and ideal for exploring computer vision interfaces.

# Gesture-Based Virtual Calculator

## Environment Setup (Important!)
Mediapipe does not fully support the latest Python versions. Please use Python 3.10 in a separate environment.

### Create a new environment:
- Using venv:
  python -m venv handcalc_env

- Or using conda:
  conda create -n handcalc_env python=3.10

### Activate the environment:
- venv:
  - Windows: handcalc_env\Scripts\activate
  - macOS/Linux: source handcalc_env/bin/activate
- conda:
  conda activate handcalc_env

### Install the dependencies:
pip install opencv-python mediapipe cvzone numpy

---

## How to Run

1. Ensure your webcam is connected.
2. Run the script:
   python aa.py

3. A calculator UI will appear on screen.
4. Use your **index finger** to tap the on-screen buttons.
5. The result will be calculated and shown instantly.

---

## Usage Tips

- Use clear and intentional tap motions.
- Ensure only the index finger is visible during use.
- Good lighting improves accuracy.
- Avoid rapid movements near the button area.

Enjoy a futuristic, touchless way of using a calculator!
