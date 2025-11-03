from PySide6.QtWidgets import QPushButton, QWidget, QVBoxLayout

class RockWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rock Widget")

        initial_button = QPushButton("Button One")
        initial_button.clicked.connect(self.functionOne)

        second_button = QPushButton("Button Two")
        second_button.clicked.connect(self.functionTwo)

      # Example of `horizontal` layout below 
      # widget_layout = QHBoxLayout()
        widget_layout = QVBoxLayout()

        widget_layout.addWidget(initial_button)
        widget_layout.addWidget(second_button)
      
        self.setLayout(widget_layout)

    
    def functionOne(self):
        pass

    def functionTwo(self):
        pass