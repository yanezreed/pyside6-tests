from sys import argv
from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader

app = QtWidgets.QApplication(argv)

loader = QUiLoader()

window = loader.load("widget.ui", None)

def print_test():
    text = window.fullName_lineEdit.text()
    if text == "":
        print("Test button clicked with no input")
    else:
        print(f"Name: {text}")
        print(f"Job:  {window.occupation_lineEdit.text()}")

window.submit_pushButton.clicked.connect(print_test)

window.show()
app.exec()