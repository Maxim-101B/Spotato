import sys
import os
from PySide6.QtWidgets import QApplication
from .ui.window import MainWindow

# Настройки DPI перед созданием QApplication
os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "0"  # Отключить high DPI scaling
os.environ["QT_SCALE_FACTOR"] = "1"           # Масштаб по умолчанию

def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.setMinimumSize(1280, 720)
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
