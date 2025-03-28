import os
import sys
import subprocess

def sanitize_filename(title):
    """Converts a title into a valid filename"""
    sanitized = title.lower().replace(' ', '_')
    return ''.join(c for c in sanitized if c.isalnum() or c == '_') + '.py'

def generate_script(title, url, filename):
    """Generates the PyQt6 browser script"""
    code = f"""
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl

class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("{title}")
        self.setGeometry(100, 100, 1200, 800)
        
        self.browser = QWebEngineView()
        self.setCentralWidget(self.browser)
        self.browser.load(QUrl("{url}"))
        self.show()  # Moved show() to __init__

def main():
    app = QApplication(sys.argv)
    window = BrowserWindow()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
"""
    with open(filename, 'w') as f:
        f.write(code.strip())

def build_executable(script_path, output_dir, exe_name):
    """Builds executable with PyInstaller and required hidden imports"""
    try:
        subprocess.run([
            'pyinstaller',
            '--onefile',
            '--windowed',
            '--name', exe_name,
            '--distpath', output_dir,
            '--hidden-import', 'PyQt6.QtWebEngineCore',
            '--hidden-import', 'PyQt6.QtNetwork',
            '--hidden-import', 'PyQt6.sip',
            script_path
        ], check=True)
        print(f"✅ Executable built successfully in: {output_dir}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Build failed: {e}")

def main():
    webapps_dir = os.path.abspath('webapps')
    os.makedirs(webapps_dir, exist_ok=True)
    
    print("🚀 Pymake")
    title = input("Enter application title: ").strip()
    url = input("Enter target URL: ").strip()
    
    script_name = sanitize_filename(title)
    script_path = os.path.join(webapps_dir, script_name)
    generate_script(title, url, script_path)
    print(f"📄 Script created: {script_path}")
    
    build_exe = input("Build executable? (y/N): ").strip().lower()
    if build_exe == 'y':
        exe_name = os.path.splitext(script_name)[0]
        print("🛠  Building executable...")
        build_executable(script_path, webapps_dir, exe_name)

if __name__ == "__main__":
    main()
