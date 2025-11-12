from PySide6.QtWidgets import QApplication, QWidget, QComboBox, QVBoxLayout, QPushButton
from sys import argv

class tab_test(QWidget):
    def __init__(self):
        super().__init__()

        self.box = QComboBox(self)

        self.box.addItem("Graves")
        self.box.addItem("Azir")
        self.box.addItem("Mundo")
        self.box.addItem("Darius")
        self.box.addItem("Luciano")

        button_current_value = QPushButton("Current Value")
        button_current_value.clicked.connect(self.current_value)
        button_set_current = QPushButton("Set value")
        button_set_current.clicked.connect(self.set_value)
        button_get_values = QPushButton("Get values")
        button_get_values.clicked.connect(self.get_values)

        layout = QVBoxLayout()
        layout.addWidget(self.box)
        layout.addWidget(button_current_value)
        layout.addWidget(button_set_current)
        layout.addWidget(button_get_values)
        layout.addSpacing(100)

        self.setLayout(layout)

    def current_value(self):
        print("Current item:", self.box.currentText())
        print("Current index:", self.box.currentIndex())
    
    def set_value(self):
        index_input = input("What index would you like? ")
        try:
            up_index = int(index_input)
        except ValueError:
            print("Input invalid")
            return
        
        temp = self.box.count()
        
        if up_index > 0 or up_index < temp:
            if up_index == 0 or up_index == temp + 1:
                self.box.setCurrentIndex(up_index)
            else:
                self.box.setCurrentIndex(up_index - 1)
        else:
            print("Input invalid")
    
    def get_values(self):
        for i in range(self.box.count()):
            print(f"index ({i}) : ", self.box.itemText(i))



def main():
    app = QApplication(argv)
    window = tab_test()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()