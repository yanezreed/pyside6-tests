# i first ran the command `pyside-uic widget.ui > ui_widget.py`
# to convert my `widget.ui` file, in my assests folder, to python code
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QApplication
from assets.ui_widget import Ui_Widget
from sys import argv

class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.submit_pushButton.clicked.connect(self.test_print)

    def test_print(self):
        print(f"name: {self.fullName_lineEdit.text()}")

app = QApplication(argv)

window = Widget()
window.show()
app.exec()