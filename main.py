from PySide6.QtWidgets import QApplication, QWidget

import sys

# Following course example...

app = QApplication(sys.argv)

window = QWidget()
window.show()

app.exec()