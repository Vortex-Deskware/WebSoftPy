# WebSoftPy 3.0 Beta 1 ✦

**Streamlined Web App Generator** - Create beautiful desktop apps from any website

## Colors
- **Purple** (Main) - `#8b5cf6`
- **Green** (Accent) - `#10b981`
- **Red** (Secondary) - `#ef4444`
- **Yellow** (Secondary) - `#f59e0b`

## Features

✨ **What's New in 3.0:**
- Modern, minimalist GUI with gradient backgrounds
- PyQt5 and PyQt6 support - choose at generation time
- Always-on persistent storage (cookies, sessions, cache)
- Two streamlined window styles: Normal OS and Frameless
- Clean, focused experience - no unnecessary complexity

## Quick Start

1. Run `WebSoftPy_v3.py`
2. Enter your app name and website URL
3. Choose Qt version (PyQt6 recommended, PyQt5 for legacy)
4. Select window style:
   - **Normal** - Standard OS title bar and window frame
   - **Frameless** - Borderless window, drag anywhere to move
5. Click "Generate App"
6. Optional: Click "Build EXE" to create a standalone executable

## Usage Guidelines

### Persistent Storage
Every generated app has persistent storage enabled by default. This means:
- Cookies are saved between sessions
- Login states are preserved
- LocalStorage/SessionStorage persists
- Cache is stored in `~/.[app_name]/`

**Important:** Do not rename your webapp after logging into websites, as this will break the storage path and you'll lose session data.

### Window Styles

**Normal (OS Title Bar)**
- Uses the native operating system window frame
- Standard minimize, maximize, and close buttons
- Fully standard behavior

**Frameless (Drag Anywhere)**
- Completely borderless window
- Click and drag anywhere to move the window
- No system controls — close via Alt+F4 or task manager

### File Structure
```
WebSoftPy 2.5/
├── WebSoftPy_v3.py          # Main application (v3.0)
├── README-v3.md             # This file
├── elements/                # App logo assets
│   └── websoftpy.png
├── pyqt/                    # Qt version logos
│   ├── pyqt5.png
│   └── pyqt6.png
└── webapps/                 # Generated apps stored here
```

## Requirements

- Python 3.8+
- PyQt6 (recommended) or PyQt5
- PyInstaller (for building executables)

```bash
# PyQt6 (Recommended)
pip install PyQt6 PyQt6-WebEngine pyinstaller

# PyQt5 (Legacy)
pip install PyQt5 PyQtWebEngine pyinstaller
```

## Generated App Features

Every generated web app includes:
- ✦ Persistent storage (cookies, cache, local data)
- ✦ Modern dark theme web view styling
- ✦ Clean, minimal code (~70-90 lines)
- ✦ No external dependencies beyond PyQt
- ✦ Works as standalone script or compiled EXE

---

## Acknowledgments

- PyQt5 and PyQt6 logos are trademarks of Riverbank Computing Ltd.
- Built with [PyQt6](https://www.riverbankcomputing.com/software/pyqt/) and [PyQt5](https://www.riverbankcomputing.com/software/pyqt/)
- Uses [PyInstaller](https://pyinstaller.org/) for executable bundling

---

© 2025 Vortex Deskware
