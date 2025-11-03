from PySide6.QtWidgets import QSlider, QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt

class RockWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rock Widget")

        self.label = QLabel("Height & Width")

        self.initial_sli = QSlider(Qt.Horizontal)
      # valueChanged signal insteaad of clicked here
        self.initial_sli.sliderReleased.connect(self.functionOne)
        self.initial_sli.setMinimum(0)
        self.initial_sli.setMaximum(100)
        self.initial_sli.setValue(25)

        self.second_sli = QSlider(Qt.Horizontal)
        self.second_sli.sliderReleased.connect(self.functionTwo)
        self.second_sli.setMinimum(0)
        self.second_sli.setMaximum(100)
        self.second_sli.setValue(25)

      # Example of `horizontal` layout below 
      # widget_layout = QHBoxLayout()
        widget_layout = QVBoxLayout()

        widget_layout.addWidget(self.label)
        widget_layout.addWidget(self.initial_sli)
        widget_layout.addWidget(self.second_sli)
      
        self.setLayout(widget_layout)

    
    def functionOne(self):
        hdata = self.initial_sli.value()
        print(f"Height = {hdata}")

    def functionTwo(self):
        wdata = self.second_sli.value()
        print(f"Width = {wdata}")