from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

def button_checked():
    print("Button checked")

# Testing checkable button
app = QApplication(sys.argv)
window = QMainWindow()
button = QPushButton()

# Remember, method is inside MainWindow class
window.setCentralWidget(button)
button.setCheckable(True)
button.clicked.connect(button_checked)

button.show
app.exec()
