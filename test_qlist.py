from PySide6.QtWidgets import QApplication, QWidget, QListWidget, QAbstractItemView, QVBoxLayout
from sys import argv

class test_list(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test List")

        self.list_widget = QListWidget(self)
        self.list_widget.setSelectionMode(QAbstractItemView.MultiSelection)
        self.list_widget.addItem("Soda")
        self.list_widget.addItems(["Coke", "Pepsi"])

        layout = QVBoxLayout()
        layout.addWidget(self.list_widget)

        self.setLayout(layout)



def main():
    app = QApplication(argv)
    window = test_list()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()
