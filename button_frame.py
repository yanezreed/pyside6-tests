from PySide6.QtWidgets import QMainWindow, QPushButton

class ButtonFrame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Button Frame")
        button = QPushButton("Press Here")
        self.setCentralWidget(button)

        # Note: need to include `self` to access the slot method
        button.clicked.connect(self.button_clicked)
    
    # Function/slot to handle button click event
    def button_clicked(self):
        print("Window button was clicked!")