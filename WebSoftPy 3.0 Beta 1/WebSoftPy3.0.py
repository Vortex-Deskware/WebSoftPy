"""
WebSoftPy 3.0 - Streamlined Web App Generator
Supports both PyQt5 and PyQt6
Colors: Purple (main), Green (accent), Red/Yellow (secondary)
"""
import sys
import shutil
import subprocess
from pathlib import Path

# ============================================================================
# QT VERSION DETECTION
# ============================================================================
def detect_qt_version():
    """Detect available Qt version and return imports."""
    # Try PyQt6 first (preferred)
    try:
        from PyQt6.QtCore import Qt, QUrl, QSize, QPoint, QSettings
        from PyQt6.QtWidgets import (
            QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
            QLabel, QLineEdit, QPushButton, QComboBox, QMessageBox, QFrame,
            QGraphicsDropShadowEffect
        )
        from PyQt6.QtGui import QFont, QPalette, QColor, QIcon, QPixmap
        return "PyQt6", True, {
            'Qt': Qt, 'QUrl': QUrl, 'QSize': QSize, 'QPoint': QPoint,
            'QApplication': QApplication, 'QMainWindow': QMainWindow,
            'QWidget': QWidget, 'QVBoxLayout': QVBoxLayout, 'QHBoxLayout': QHBoxLayout,
            'QLabel': QLabel, 'QLineEdit': QLineEdit, 'QPushButton': QPushButton,
            'QComboBox': QComboBox, 'QMessageBox': QMessageBox, 'QFrame': QFrame,
            'QGraphicsDropShadowEffect': QGraphicsDropShadowEffect,
            'QFont': QFont, 'QPalette': QPalette, 'QColor': QColor,
            'QIcon': QIcon, 'QPixmap': QPixmap, 'QSettings': QSettings,
        }
    except ImportError:
        pass
    
    # Fall back to PyQt5
    try:
        from PyQt5.QtCore import Qt, QUrl, QSize, QPoint, QSettings
        from PyQt5.QtWidgets import (
            QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
            QLabel, QLineEdit, QPushButton, QComboBox, QMessageBox, QFrame,
            QGraphicsDropShadowEffect
        )
        from PyQt5.QtGui import QFont, QPalette, QColor, QIcon, QPixmap
        return "PyQt5", False, {
            'Qt': Qt, 'QUrl': QUrl, 'QSize': QSize, 'QPoint': QPoint,
            'QApplication': QApplication, 'QMainWindow': QMainWindow,
            'QWidget': QWidget, 'QVBoxLayout': QVBoxLayout, 'QHBoxLayout': QHBoxLayout,
            'QLabel': QLabel, 'QLineEdit': QLineEdit, 'QPushButton': QPushButton,
            'QComboBox': QComboBox, 'QMessageBox': QMessageBox, 'QFrame': QFrame,
            'QGraphicsDropShadowEffect': QGraphicsDropShadowEffect,
            'QFont': QFont, 'QPalette': QPalette, 'QColor': QColor,
            'QIcon': QIcon, 'QPixmap': QPixmap, 'QSettings': QSettings,
        }
    except ImportError:
        pass
    
    # No Qt found
    return None, False, {}


QT_VERSION, IS_PYQT6, QT_LIBS = detect_qt_version()

if QT_VERSION is None:
    print("ERROR: Neither PyQt6 nor PyQt5 is installed.")
    print("Please install one of the following:")
    print("  PyQt6: pip install PyQt6 PyQt6-WebEngine")
    print("  PyQt5: pip install PyQt5 PyQtWebEngine")
    sys.exit(1)

# Extract commonly used items
Qt = QT_LIBS['Qt']
QFont = QT_LIBS['QFont']
QColor = QT_LIBS['QColor']
QIcon = QT_LIBS['QIcon']
QPixmap = QT_LIBS['QPixmap']
QPalette = QT_LIBS['QPalette']
QApplication = QT_LIBS['QApplication']
QMainWindow = QT_LIBS['QMainWindow']
QWidget = QT_LIBS['QWidget']
QVBoxLayout = QT_LIBS['QVBoxLayout']
QHBoxLayout = QT_LIBS['QHBoxLayout']
QLabel = QT_LIBS['QLabel']
QLineEdit = QT_LIBS['QLineEdit']
QPushButton = QT_LIBS['QPushButton']
QComboBox = QT_LIBS['QComboBox']
QMessageBox = QT_LIBS['QMessageBox']
QFrame = QT_LIBS['QFrame']
QGraphicsDropShadowEffect = QT_LIBS['QGraphicsDropShadowEffect']


# ============================================================================
# COLOR SCHEME
# ============================================================================
COLORS = {
    "bg_dark": "#1a1a2e",
    "bg_card": "#16213e",
    "bg_input": "#0f3460",
    "purple_main": "#8b5cf6",
    "purple_light": "#a78bfa",
    "purple_dark": "#7c3aed",
    "green_accent": "#10b981",
    "green_light": "#34d399",
    "red_accent": "#ef4444",
    "yellow_accent": "#f59e0b",
    "text_primary": "#f8fafc",
    "text_secondary": "#94a3b8",
    "border": "#334155",
}


def sanitize_filename(title: str) -> str:
    """Convert title to valid filename."""
    sanitized = title.lower().replace(' ', '_')
    return ''.join(c for c in sanitized if c.isalnum() or c == '_')


def copy_elements_to_webapps():
    """Copy elements folder to webapps directory (kept for legacy compatibility)."""
    script_dir = Path(__file__).parent.resolve()
    src_elements = script_dir / "elements"
    webapps_dir = script_dir / "webapps"
    dest_elements = webapps_dir / "elements"

    if not webapps_dir.exists():
        webapps_dir.mkdir(exist_ok=True)


def generate_webapp_script(title: str, url: str, qt_version: str, window_style: str, filename: str):
    """Generate the web app Python script."""
    url = url.strip()
    sanitized_name = sanitize_filename(title)

    # Qt imports based on version
    is_pyqt5 = qt_version == "PyQt5"

    if is_pyqt5:
        # PyQt5 imports
        base_imports = """import sys
from pathlib import Path
from PyQt5.QtCore import Qt, QUrl, QPoint
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QGraphicsDropShadowEffect
)
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQtWebEngine.QtWebEngineCore import QWebEnginePage, QWebEngineProfile
"""
        # PyQt5 enum access
        left_button = "Qt.LeftButton"
        frameless_hint = "Qt.FramelessWindowHint"
        global_pos_method = "globalPos()"
    else:
        # PyQt6 imports
        base_imports = """import sys
from pathlib import Path
from PyQt6.QtCore import Qt, QUrl, QPoint
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QGraphicsDropShadowEffect
)
from PyQt6.QtGui import QFont, QColor
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebEngineCore import QWebEnginePage, QWebEngineProfile
"""
        # PyQt6 enum access
        left_button = "Qt.MouseButton.LeftButton"
        frameless_hint = "Qt.WindowType.FramelessWindowHint"
        global_pos_method = "globalPosition().toPoint()"

    # Check window style
    use_normal_titlebar = window_style == "normal"

    # Persistent storage code (always enabled)
    storage_code = f'''
        try:
            profile = QWebEngineProfile("CustomProfile", self)
            profile.setPersistentCookiesPolicy(QWebEngineProfile.PersistentCookiesPolicy.ForcePersistentCookies)
            profile.setCachePath(str(Path.home() / ".{sanitized_name}" / "cache"))
            profile.setPersistentStoragePath(str(Path.home() / ".{sanitized_name}" / "storage"))
            page = QWebEnginePage(profile, self)
            self.webview.setPage(page)
        except Exception as e:
            print(f"Warning: Profile initialization failed: {{e}}")
            # Fallback to default profile
            page = QWebEnginePage(self)
            self.webview.setPage(page)
'''

    # Main browser class - different for each window style
    if use_normal_titlebar:
        # Normal window with OS title bar
        browser_class = f'''

class SingleSiteBrowser(QMainWindow):
    def __init__(self, start_url: str, app_title: str):
        super().__init__()

        self.setWindowTitle(app_title)
        self.setMinimumSize(1000, 700)

        # Web view
        self.webview = QWebEngineView()
{storage_code}
        self.webview.setUrl(QUrl(start_url))

        # Apply modern web view styling
        self.webview.setStyleSheet("""
            QWebEngineView {{
                background-color: #0f172a;
                border: none;
            }}
        """)

        self.setCentralWidget(self.webview)
'''
    else:
        # Frameless window (no controls)
        browser_class = f'''

class SingleSiteBrowser(QMainWindow):
    def __init__(self, start_url: str, app_title: str):
        super().__init__()

        # Frameless window
        self.setWindowFlags({frameless_hint})
        self.setMinimumSize(1000, 700)

        self._drag_pos = QPoint()

        # Web view
        self.webview = QWebEngineView()
{storage_code}
        self.webview.setUrl(QUrl(start_url))

        # Apply modern web view styling
        self.webview.setStyleSheet("""
            QWebEngineView {{
                background-color: #0f172a;
                border: none;
            }}
        """)

        self.setCentralWidget(self.webview)

    def mousePressEvent(self, event):
        if event.button() == {left_button}:
            self._drag_pos = event.{global_pos_method}

    def mouseMoveEvent(self, event):
        if event.buttons() == {left_button}:
            diff = event.{global_pos_method} - self._drag_pos
            self.move(self.pos() + diff)
            self._drag_pos = event.{global_pos_method}
'''

    # Build the final code
    code = f"""{base_imports}
{browser_class}

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("{title}")

    window = SingleSiteBrowser("{url}", "{title}")
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
"""

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(code.strip())


# ============================================================================
# MAIN GUI
# ============================================================================
class WebSoftPyGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WebSoftPy 3.0")
        self.setMinimumSize(650, 550)
        self.setMaximumSize(900, 800)

        # Get folder paths for logos
        self.pyqt_dir = Path(__file__).parent.resolve() / "pyqt"
        self.elements_dir = Path(__file__).parent.resolve() / "elements"

        self.setup_ui()
        self.apply_theme()

        self.generated_script = None
        self.webapps_dir = Path("webapps").resolve()
        self.webapps_dir.mkdir(exist_ok=True)

    def setup_ui(self):
        """Setup the main UI."""
        central = QWidget()
        main_layout = QVBoxLayout(central)
        main_layout.setSpacing(16)
        main_layout.setContentsMargins(40, 25, 40, 25)

        # ============ HEADER ============
        header_layout = QHBoxLayout()
        header_layout.setSpacing(12)

        # Title
        title_label = QLabel("WebSoftPy 3.0")
        title_label.setFont(QFont("Segoe UI", 24, QFont.Weight.Bold if IS_PYQT6 else QFont.Bold))
        title_label.setStyleSheet("color: #8b5cf6;")
        header_layout.addWidget(title_label)

        header_layout.addStretch()

        # Qt version logo (dynamic based on selection)
        self.qt_logo_label = QLabel()
        self.qt_logo_label.setFixedSize(120, 50)
        self.qt_logo_label.setStyleSheet("padding: 4px;")
        # Will update after qt_combo is created
        header_layout.addWidget(self.qt_logo_label)

        main_layout.addLayout(header_layout)

        # Subtitle
        subtitle = QLabel("Create beautiful desktop apps from any website")
        subtitle.setStyleSheet("color: #94a3b8; font-size: 13px;")
        main_layout.addWidget(subtitle)

        # Separator
        separator = QFrame()
        if IS_PYQT6:
            separator.setFrameShape(QFrame.Shape.HLine)
        else:
            separator.setFrameShape(QFrame.HLine)
        separator.setStyleSheet("background: #334155; min-height: 2px; max-height: 2px;")
        main_layout.addWidget(separator)

        # ============ FORM FIELDS ============
        # App Name
        main_layout.addWidget(self.create_label("Application Name"))
        self.title_input = self.create_input("e.g., My Awesome App")
        main_layout.addWidget(self.title_input)

        # URL
        main_layout.addWidget(self.create_label("Website URL"))
        self.url_input = self.create_input("https://example.com")
        main_layout.addWidget(self.url_input)

        # Qt Version
        main_layout.addWidget(self.create_label("Qt Version"))
        self.qt_combo = QComboBox()
        self.qt_combo.addItems([f"PyQt6 (Recommended)", f"PyQt5 (Legacy)"])
        self.qt_combo.currentIndexChanged.connect(self.on_qt_version_changed)
        self.qt_combo.setStyleSheet(self.get_input_style())
        main_layout.addWidget(self.qt_combo)

        # Initialize Qt logo after qt_combo exists
        self.update_qt_logo()

        # Window Style
        main_layout.addWidget(self.create_label("Window Style"))
        self.style_combo = QComboBox()
        self.style_combo.addItems([
            "Normal (OS Title Bar)",
            "Frameless (Drag Anywhere to Move)"
        ])
        self.style_combo.currentIndexChanged.connect(self.on_style_changed)
        self.style_combo.setStyleSheet(self.get_input_style())
        main_layout.addWidget(self.style_combo)

        # Style info label
        self.style_info_label = QLabel("")
        self.style_info_label.setWordWrap(True)
        self.style_info_label.setStyleSheet("color: #94a3b8; font-size: 12px; padding: 10px; background: #0f3460; border-radius: 8px;")
        main_layout.addWidget(self.style_info_label)

        # ============ SPACER ============
        main_layout.addStretch(1)

        # ============ INFO CARD ============
        info_card = QFrame()
        info_card.setStyleSheet("""
            QFrame {
                background: #0f3460;
                border: 1px solid #334155;
                border-radius: 12px;
                padding: 14px 18px;
            }
        """)
        info_layout = QVBoxLayout(info_card)
        info_layout.setSpacing(6)

        info_title = QLabel("✨ Features")
        info_title.setFont(QFont("Segoe UI", 11, QFont.Weight.Bold if IS_PYQT6 else QFont.Bold))
        info_title.setStyleSheet("color: #10b981;")
        info_layout.addWidget(info_title)

        info_text = QLabel(
            "• Persistent storage enabled by default (cookies, sessions)\n"
            "• Clean, streamlined interface\n"
            "• Build standalone executables with PyInstaller"
        )
        info_text.setStyleSheet("color: #94a3b8; font-size: 12px; line-height: 1.5;")
        info_text.setWordWrap(True)
        info_layout.addWidget(info_text)

        main_layout.addWidget(info_card)

        # ============ ACTION BUTTONS ============
        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(16)

        self.gen_btn = self.create_button("💾 Generate App", "#8b5cf6")
        self.gen_btn.clicked.connect(self.generate)
        btn_layout.addWidget(self.gen_btn)

        self.build_btn = self.create_button("🛠️ Build EXE", "#10b981")
        self.build_btn.clicked.connect(self.build_exe)
        self.build_btn.setEnabled(False)
        btn_layout.addWidget(self.build_btn)

        main_layout.addLayout(btn_layout)

        # Status bar area
        self.status_label = QLabel("")
        self.status_label.setStyleSheet("color: #94a3b8; font-size: 11px;")
        self.status_label.setWordWrap(True)
        main_layout.addWidget(self.status_label)

        self.setCentralWidget(central)

        # Initialize visibility
        self.on_qt_version_changed()
        self.on_style_changed()

    def create_label(self, text):
        """Create a styled label."""
        label = QLabel(text)
        if IS_PYQT6:
            label.setFont(QFont("Segoe UI", 11, QFont.Weight.SemiBold if hasattr(QFont.Weight, 'SemiBold') else QFont.Weight.Bold))
        else:
            label.setFont(QFont("Segoe UI", 11, QFont.Bold))
        label.setStyleSheet("color: #f8fafc; margin-bottom: 6px;")
        return label

    def create_input(self, placeholder):
        """Create a styled input field."""
        input_field = QLineEdit()
        input_field.setPlaceholderText(placeholder)
        input_field.setStyleSheet(self.get_input_style())
        return input_field

    def get_input_style(self):
        """Get input field stylesheet."""
        return """
            QLineEdit {{
                background: #0f3460;
                color: #f8fafc;
                border: 2px solid #334155;
                border-radius: 10px;
                padding: 12px 16px;
                font-size: 13px;
                font-family: "Segoe UI", sans-serif;
            }}
            QLineEdit:focus {{
                border: 2px solid #8b5cf6;
                background: #1a4a7a;
            }}
            QLineEdit::placeholder {{
                color: #64748b;
            }}
        """

    def create_button(self, text, color):
        """Create a styled button."""
        btn = QPushButton(text)
        btn.setFont(QFont("Segoe UI", 12, QFont.Weight.Bold if IS_PYQT6 else QFont.Bold))
        if IS_PYQT6:
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
        else:
            btn.setCursor(Qt.PointingHandCursor)
        btn.setStyleSheet(f"""
            QPushButton {{
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 {color}, stop:1 {self.lighten_color(color)});
                color: white;
                border: none;
                border-radius: 12px;
                padding: 14px 24px;
                min-width: 150px;
            }}
            QPushButton:hover {{
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 {self.lighten_color(color)}, stop:1 {color});
            }}
            QPushButton:pressed {{
                background: {color};
            }}
            QPushButton:disabled {{
                background: #334155;
                color: #64748b;
            }}
        """)
        return btn

    def lighten_color(self, color):
        """Lighten a hex color."""
        if color == "#8b5cf6":
            return "#a78bfa"
        elif color == "#10b981":
            return "#34d399"
        return color

    def apply_theme(self):
        """Apply the main application theme."""
        self.setStyleSheet("""
            QMainWindow {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #1a1a2e, stop:1 #0f172a);
            }
            QComboBox {{
                background: #0f3460;
                color: #f8fafc;
                border: 2px solid #334155;
                border-radius: 10px;
                padding: 10px 14px;
                font-size: 13px;
                font-family: "Segoe UI", sans-serif;
            }}
            QComboBox:hover {{
                border: 2px solid #8b5cf6;
            }}
            QComboBox::drop-down {{
                border: none;
                width: 30px;
            }}
            QComboBox::down-arrow {{
                width: 12px;
                height: 12px;
            }}
            QComboBox QAbstractItemView {{
                background: #0f3460;
                color: #f8fafc;
                border: 2px solid #334155;
                border-radius: 10px;
                selection-background-color: #8b5cf6;
                outline: none;
            }}
            QScrollBar:vertical {{
                background: #1a1a2e;
                width: 10px;
                border-radius: 5px;
            }}
            QScrollBar::handle:vertical {{
                background: #334155;
                border-radius: 5px;
                min-height: 20px;
            }}
            QScrollBar::handle:vertical:hover {{
                background: #8b5cf6;
            }}
            QMessageBox {{
                background-color: #1a1a2e;
                color: #f8fafc;
            }}
            QMessageBox QLabel {{
                color: #f8fafc;
                font-size: 13px;
            }}
            QMessageBox QPushButton {{
                background: #8b5cf6;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 10px 20px;
                min-width: 80px;
                font-weight: bold;
            }}
            QMessageBox QPushButton:hover {{
                background: #a78bfa;
            }}
        """)

    def get_qt_version(self):
        """Get selected Qt version."""
        idx = self.qt_combo.currentIndex()
        return "PyQt5" if idx == 1 else "PyQt6"

    def update_qt_logo(self):
        """Update the Qt logo based on selected version."""
        is_pyqt5 = self.qt_combo.currentIndex() == 1
        logo_file = "pyqt5.png" if is_pyqt5 else "pyqt6.png"
        logo_path = self.pyqt_dir / logo_file

        if logo_path.exists():
            pixmap = QPixmap(str(logo_path))
            scaled_pixmap = pixmap.scaled(
                100, 40,
                Qt.AspectRatioMode.KeepAspectRatio if IS_PYQT6 else Qt.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation if IS_PYQT6 else Qt.SmoothTransformation
            )
            self.qt_logo_label.setPixmap(scaled_pixmap)
            self.qt_logo_label.setAlignment(
                Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter if IS_PYQT6
                else Qt.AlignRight | Qt.AlignVCenter
            )
        else:
            version_text = "PyQt5" if is_pyqt5 else "PyQt6"
            self.qt_logo_label.setText(version_text)
            self.qt_logo_label.setStyleSheet("""
                background: #10b981;
                color: #1a1a2e;
                padding: 6px 14px;
                border-radius: 20px;
                font-weight: bold;
                font-size: 11px;
            """)

    def on_qt_version_changed(self):
        """Handle Qt version change."""
        self.update_qt_logo()
        self.on_style_changed()

    def on_style_changed(self):
        """Handle window style change."""
        idx = self.style_combo.currentIndex()

        if idx == 0:
            self.style_info_label.setText("Uses the native operating system window frame. Standard behavior.")
        else:
            self.style_info_label.setText("Completely borderless window. Drag anywhere to move. Close via Alt+F4 or task manager.")

    def get_window_style(self):
        """Get selected window style."""
        idx = self.style_combo.currentIndex()
        return "normal" if idx == 0 else "frameless"

    def generate(self):
        """Generate the web app script."""
        title = self.title_input.text().strip()
        url = self.url_input.text().strip()
        qt_version = self.get_qt_version()
        window_style = self.get_window_style()

        # Validation
        if not title:
            self.show_message("Warning", "Please enter an application name.", "warning")
            return
        if not url:
            self.show_message("Warning", "Please enter a website URL.", "warning")
            return
        if not url.startswith(("http://", "https://")):
            self.show_message("Invalid URL", "URL must start with http:// or https://", "warning")
            return

        filename_base = sanitize_filename(title)
        if not filename_base:
            self.show_message("Invalid Name", "Please use a valid application name.", "warning")
            return

        script_path = self.webapps_dir / f"{filename_base}.py"

        try:
            generate_webapp_script(title, url, qt_version, window_style, script_path)
            self.generated_script = script_path
            self.build_btn.setEnabled(True)
            self.status_label.setText(f"✓ Generated: {script_path.name}")
            self.status_label.setStyleSheet("color: #10b981; font-size: 12px; font-weight: bold;")
            self.show_message("Success!", f"Web app script generated!\n\n{script_path}", "info")
        except Exception as e:
            self.show_message("Generation Failed", f"Error: {str(e)}", "critical")

    def build_exe(self):
        """Build executable with PyInstaller."""
        if not self.generated_script or not self.generated_script.exists():
            return

        exe_name = self.generated_script.stem
        output_dir = self.webapps_dir

        reply = QMessageBox.question(
            self,
            "Build Executable?",
            f"Build standalone .exe for '{exe_name}'?\n\nThis may take 1–3 minutes.",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        if reply != QMessageBox.Yes:
            return

        try:
            cmd = [
                sys.executable, '-m', 'PyInstaller',
                '--onefile',
                '--windowed',
                '--name', exe_name,
                '--distpath', str(output_dir),
                '--hidden-import', 'PyQt6.QtWebEngineCore' if QT_VERSION == "PyQt6" else 'PyQtWebEngine.QtWebEngineCore',
                '--hidden-import', 'PyQt6.QtNetwork' if QT_VERSION == "PyQt6" else 'PyQt5.QtNetwork',
                '--hidden-import', 'PyQt6.sip' if QT_VERSION == "PyQt6" else 'PyQt5.sip',
            ] + [str(self.generated_script)]

            subprocess.run(cmd, check=True, capture_output=True)

            self.status_label.setText(f"✓ EXE built: {output_dir / exe_name}.exe")
            self.status_label.setStyleSheet("color: #10b981; font-size: 12px; font-weight: bold;")

            self.show_message(
                "Build Complete! 🎉",
                f"Executable created successfully!\n\nLocation:\n{output_dir / exe_name}.exe",
                "info"
            )
        except subprocess.CalledProcessError as e:
            error_msg = f"PyInstaller error.\n\nStderr:\n{e.stderr.decode() if e.stderr else 'Unknown error'}"
            self.show_message("Build Failed", error_msg, "critical")
        except FileNotFoundError:
            self.show_message("Missing Dependency", "PyInstaller is not installed.\n\nRun: pip install pyinstaller", "warning")
        except Exception as e:
            self.show_message("Build Failed", f"Unexpected error: {str(e)}", "critical")

    def show_message(self, title, message, msg_type="info"):
        """Show a message box."""
        if msg_type == "warning":
            QMessageBox.warning(self, title, message)
        elif msg_type == "critical":
            QMessageBox.critical(self, title, message)
        else:
            QMessageBox.information(self, title, message)


# ============================================================================
# ENTRY POINT
# ============================================================================
def main():
    # Copy elements to webapps (kept for legacy compatibility)
    copy_elements_to_webapps()

    # Create application
    app = QApplication(sys.argv)
    app.setApplicationName("WebSoftPy 3.0")

    # Apply dark palette (compatible with both PyQt5 and PyQt6)
    dark_palette = QPalette()

    # Handle PyQt5 vs PyQt6 color role differences
    if IS_PYQT6:
        Window = QPalette.ColorRole.Window
        WindowText = QPalette.ColorRole.WindowText
        Base = QPalette.ColorRole.Base
        AlternateBase = QPalette.ColorRole.AlternateBase
        ToolTipBase = QPalette.ColorRole.ToolTipBase
        ToolTipText = QPalette.ColorRole.ToolTipText
        Text = QPalette.ColorRole.Text
        Button = QPalette.ColorRole.Button
        ButtonText = QPalette.ColorRole.ButtonText
        BrightText = QPalette.ColorRole.BrightText
        Link = QPalette.ColorRole.Link
        Highlight = QPalette.ColorRole.Highlight
        HighlightedText = QPalette.ColorRole.HighlightedText
    else:
        Window = QPalette.Window
        WindowText = QPalette.WindowText
        Base = QPalette.Base
        AlternateBase = QPalette.AlternateBase
        ToolTipBase = QPalette.ToolTipBase
        ToolTipText = QPalette.ToolTipText
        Text = QPalette.Text
        Button = QPalette.Button
        ButtonText = QPalette.ButtonText
        BrightText = QPalette.BrightText
        Link = QPalette.Link
        Highlight = QPalette.Highlight
        HighlightedText = QPalette.HighlightedText

    dark_palette.setColor(Window, QColor(26, 26, 46))
    dark_palette.setColor(WindowText, QColor(248, 250, 252))
    dark_palette.setColor(Base, QColor(15, 52, 96))
    dark_palette.setColor(AlternateBase, QColor(22, 33, 62))
    dark_palette.setColor(ToolTipBase, QColor(248, 250, 252))
    dark_palette.setColor(ToolTipText, QColor(248, 250, 252))
    dark_palette.setColor(Text, QColor(248, 250, 252))
    dark_palette.setColor(Button, QColor(22, 33, 62))
    dark_palette.setColor(ButtonText, QColor(248, 250, 252))
    dark_palette.setColor(BrightText, QColor(16, 185, 129))
    dark_palette.setColor(Link, QColor(139, 92, 246))
    dark_palette.setColor(Highlight, QColor(139, 92, 246))
    dark_palette.setColor(HighlightedText, QColor(26, 26, 46))
    app.setPalette(dark_palette)

    # Show main window
    window = WebSoftPyGUI()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
