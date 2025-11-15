from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtGui import QIcon
from assets.ui_widget import Ui_Widget
from sys import argv

import assets.resource_rc as resource_rc

class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # accessed via `Ui_Widget`, `objectName` = spin_box
        self.spin_box.setValue(50)

        # note; i dont need to create any objects as the already exist within `Ui_Widget`
        self.plus_button.clicked.connect(self.plus)
        self.minus_button.clicked.connect(self.minus)

        plus_icon = QIcon("::\OneDrive\Pictures\plus.png") # <- dont want to give anymore info!
        minus_icon = QIcon(":\OneDrive\Pictures\minus.png") # this is for example only

        self.plus_button.setIcon(plus_icon)
        self.minus_button.setIcon(minus_icon)

        # note; here i am accessing the `QPushButtons`` within `Ui_Widget`` via `self`
        # (within the class), using `setIcon()` im able to apply the `QIcon`s above
        # note i am assigning the objects and not the class itself

    def plus(self):
        value = self.spin_box.value()
        self.spin_box.setValue(value + 1)
        # here when the button is clicked, im grabbing its value and `setValue` to plus one

    def minus(self):
        value = self.spin_box.value()
        self.spin_box.setValue(value - 1)
        # same process again, only minus one

app = QApplication(argv)

window = Widget()
window.show()
app.exec()