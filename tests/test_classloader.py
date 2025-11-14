from sys import argv
from PySide6 import QtCore, QtWidgets
from PySide6.QtUiTools import QUiLoader

app = QtWidgets.QApplication(argv)
loader = QUiLoader()

class UserInterface(QtCore.QObject):
    def __init__(self):
        super().__init__()
        self.ui = loader.load("assets\widget.ui", None)
        self.ui.submit_pushButton.clicked.connect(self.print_test)

    def show(self):
        self.ui.show()

    def print_test(self):
        name = self.ui.fullName_lineEdit.text()
        job = self.ui.occupation_lineEdit.text()

        if name == "":
            print("Test button clicked with no input")
        else:
            print(f"Name: {name}")
            print(f"Job:  {job}")


window = UserInterface()
window.show()

app.exec()