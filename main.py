from PySide6.QtWidgets import QApplication
from button_frame import ButtonFrame 
import sys

# Following course example...
app = QApplication(sys.argv)
window = ButtonFrame()
window.show()
app.exec()

# Structure: app -> window(external file) -> button(external file)