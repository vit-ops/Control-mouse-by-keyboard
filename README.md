# 🖱️ MouseArrow Pro

Control your mouse using only the keyboard. A lightweight Python desktop application with a modern UI, global hotkeys, smooth acceleration, and automatic EXE generation.

# 🚀 Features

Toggle mouse control with F9

Move the cursor using arrow keys

Progressive acceleration while moving

Precision movement using Shift

Left and right mouse clicks via keyboard

Vertical scroll control

Modern dark-mode interface

Always-on-top window

Automatic dependency installation

One-click .exe generation

# 🎮 Keyboard Controls
Activation

F9 → Enable / Disable MouseArrow

Mouse Movement

Arrow Keys → Move cursor

Shift + Arrow Keys → Slow and precise movement

Mouse Clicks

/ → Left click

* → Right click

(Works with both standard and numpad keyboards)

Scrolling

+ → Scroll up

- → Scroll down

# 🖥️ Interface

Main toggle button (ON / OFF)

Status indicator

INSTALL (.EXE) button (only visible when running the .py script)

Window stays always on top for quick access

# 🛠️ Technologies Used

Python 3

CustomTkinter – Modern GUI

PyAutoGUI – Mouse control

Keyboard – Global hotkeys

PyInstaller – Executable generation

Threading – Smooth background execution

# 📦 Installation & Usage
Run from Python
```bash

python mousearrow.py
```

All required dependencies are installed automatically on first run.

Generate Executable (.exe)

Run the .py file

Click INSTALL (.EXE)

Wait for the process to finish

The executable will be available in the dist/ folder

⚠️ Notes

After generating the executable, it can be found in the dist directory. All other folders are unnecessary.

PyAutoGUI failsafe is enabled (moving the mouse to a screen corner stops execution).

The app runs without a console window.

The EXE generation button is hidden when running the compiled version.

📌 Use Cases

Accessibility support

Mouse-free navigation

Automation experiments

Backup control when mouse hardware fails

Learning input automation with Python
