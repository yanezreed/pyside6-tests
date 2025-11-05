from PySide6.QtWidgets import QApplication
from mainwindow import MainWindow
from sys import argv

app = QApplication(argv)

# Here is where i pass in app!
window = MainWindow(app)
window.show()
app.exec()








































# Second Version

# from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
# from rock_widget import RockWidget
# import sys

# app = QApplication(sys.argv)

# window = RockWidget()
# window.setFixedSize(300, 200)

# window.show()
# app.exec()



# First Version

# from PySide6.QtWidgets import QApplication
# from button_frame import ButtonFrame 
# import sys

# Following course example...
# app = QApplication(sys.argv)
# window = ButtonFrame()
# window.show()
# app.exec()

# Structure: app -> window(external file) -> button(external file)"