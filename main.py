from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

# Following course example...

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        button = QPushButton("Click Me")
        self.setCentralWidget(button)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

# Structure: app -> window -> button