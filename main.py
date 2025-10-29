from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

# Following course example...

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("My App")

button = QPushButton("Click Me")
window.setCentralWidget(button)
window.show()

app.exec()