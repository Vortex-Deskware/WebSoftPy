# Turn any website into a desktop app. Fast, flexible, yours. That's WebSoftPy.

![r2-final-transparent](https://github.com/user-attachments/assets/745fefe2-aa95-4d47-b0c1-d9d9ca625186)

## Prerequisites

---

- ```pip install PyQt6 PyQt6-WebEngine pyinstaller``` |For 1.0 Full Release onwards.

  **Or** run the included batch script (If you are on Windows).

---

- ```pip install PyQt5 PyQtWebEngine pyinstaller```  |For 1.0 Pre-Release (Legacy)


---
# Usage

WebSoftPy is a desktop application that converts any website into a standalone desktop web app using PyQt6 and Qt WebEngine.

## How to Use

1. **Fill in the details**:  
   - **Application Title**: The name of your web app (e.g., "My WebSoftPy App").  
   - **Target URL**: The full `https://` (or `http://`) address of the site.  
   - **Window Style**: Choose from:
     - *Normal*: Standard OS window.  
     - *Custom Title Bar*: Frameless window with draggable title bar and **theme-based SVG controls**.  
     - *Frameless Window*: Borderless, draggable window with no buttons.  
   - **Theme** *(visible only for “Custom Title Bar”)*: Select a visual style:  
     - *WebSoftPy Flow* (original)  
     - *WebSoftPy Desk* (minimal)  
     - *WebSoftPy Color* (colored icons)  
     - *WebSoftPy Fizz* (bubble-inspired)  
     - *WebSoftPy Text* (text-based labels)  
     - *WebSoftPy Draw* (hand-drawn style)  
   - **Persistent Storage**: Enable to save cookies, cache, and local data between sessions.

2. **Generate the app**:  
   Click **"Generate Web App"**. A `.py` script will be saved in the `webapps/` folder.

3. **(Optional) Build an executable**:  
   Click **"Build Executable"** to create a standalone `.exe` (Windows) or binary (macOS/Linux) using PyInstaller.  
   > ⚠️ This requires `pyinstaller` to be installed (`pip install pyinstaller`).

4. **Run your app**:  
   - Use the `.py` file directly (requires Python + PyQt6).  
   - Or run the generated executable for portability.

---

### File Structure

After generation, your project directory will look like this:

```
your_project/
├── WebSoftPy.py        ← Generator (run this)
├── elements/               ← Theme assets
│   ├── WebSoftPy Flow/
│   │   ├── minimize.svg
│   │   ├── maximize.svg
│   │   └── close.svg
│   ├── WebSoftPy Desk/
│   ├── WebSoftPy Color/
│   ├── WebSoftPy Fizz/
│   ├── WebSoftPy Text/
│   └── WebSoftPy Draw/
└── webapps/                ← Generated apps go here
    ├── my_app.py           ← Source code
    └── my_app/             ← Executable (if built)
        └── my_app.exe
```

> **Important**:  
> - Do **not move** generated apps outside the `webapps/` folder—this breaks SVG icon paths.  
> - Do **not rename** a webapp after logging in—this will reset persistent storage and delete cookies.  
> - For easy access, create desktop shortcuts instead.

---

## How the Generator Looks

The WebSoftPy GUI provides a clean, dark-themed interface:

- Input fields for title and URL  
- Dropdown to select window style  
- **Theme selector** (appears when “Custom Title Bar” is chosen)  
- Dynamic description of the selected mode  
- Toggle for persistent storage  
- One-click generation and build buttons  

<img width="622" height="552" alt="image" src="https://github.com/user-attachments/assets/0289cada-bd4b-4a95-bdb6-18a34644e2f3" />


---

## Notes from Developers

- WebSoftPy is actively maintained and will receive usability improvements (e.g., automatic shortcut creation).  
- The tool is generic, no site is hardcoded. It works with any valid URL.  
- Generated apps are fully self-contained and respect user privacy settings.  
- Version 2.5 introduces **Expressional** theming, let your desktop reflect your style.

---

### Frequently Asked Questions

**Q: Why are `.exe` files so large (~150 MB)?**  
A: PyInstaller bundles the Python interpreter, PyQt6, Qt WebEngine, and all dependencies. To reduce size, compress the executable with [UPX](https://upx.github.io/), a free and secure executable packer that typically reduces file size by 50–70% with no runtime penalty.

**Q: What license is WebSoftPy under?**  
A: WebSoftPy is licensed under the **Apache License 2.0**. See the `LICENSE` file for details.

**Q: Can I customize the title bar buttons?**  
A: Yes. Each theme has its own folder in `elements/`. You can edit or replace the SVGs in any theme folder (e.g., `elements/WebSoftPy Desk/minimize.svg`). Just keep the filenames unchanged.

---

Vortex Deskware © 2025  
*WebSoftPy 2.5 Full Release | Expressional*
