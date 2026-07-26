# OpenCV Interactive Drawing App

An interactive Python application built with **OpenCV** and **NumPy** that allows users to draw shapes and paint on a digital canvas using mouse events and keyboard shortcuts.

---

## Libraries Used

* **numpy** (`numpy`)
* **OpenCV** (`cv2`)
* **random** (Python built-in)

---

## Installation

Ensure you have Python installed, then install the required dependencies using pip:

```cmd
pip install numpy opencv-python
```

## Controls & Shortcuts

* Left Click (Circle mode): Draws a filled circle at the cursor location.
* Left Click (Rectangle mode): First click sets the starting point (ix, iy); second click draws the rectangle.
* Right Click: Changes the current drawing color to a random RGB value.
* c: Switch drawing mode to Circle.
* r: Switch drawing mode to Rectangle.
* s: Save the current canvas as an image (output_0.jpg, output_1.jpg, etc.).
* q: Quit and close the application.
