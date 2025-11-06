from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox
from sys import argv

class TestWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Test Button Widget")

        button = QPushButton("Test")
        button.clicked.connect(self.button_clicked)
        button.pressed.connect(self.button_pressed)
        button.released.connect(self.button_released)

        layout = QVBoxLayout()
        layout.addWidget(button)
        self.setLayout(layout)

    def button_clicked(self):
        print("Clicked")
    def button_pressed(self):
        print("Pressed")
    def button_released(self):
        print("Released")


app = QApplication(argv)
window = TestWidget()
window.show()
app.exec()