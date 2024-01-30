import sys

from PySide6.QtWidgets import QApplication

from windows import StartWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StartWindow()
    window.show()

    sys.exit(app.exec())
