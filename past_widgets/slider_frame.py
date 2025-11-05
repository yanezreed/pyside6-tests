from PySide6.QtWidgets import QMainWindow, QSlider
from PySide6.QtCore import Qt

class SliderFrame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Slider Frame")

        # Creates a customized slider form QtCore

        slider = QSlider(Qt.Horizontal)
        self.setCentralWidget(slider)

        slider.setMinimum(0)
        slider.setMaximum(100)
        slider.setValue(25)

        # I need to remember to always call functions with `self`

        slider.valueChanged.connect(self.slider_data)

    def slider_data(self, data):
        print("slider moved to:", data)