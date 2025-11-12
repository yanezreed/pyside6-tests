from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QHBoxLayout, QTabWidget, QVBoxLayout, QPushButton
from sys import argv

class tab_test(QWidget):
    def __init__(self):
        super().__init__()
        
        tab_itself = QTabWidget(self)

        widget_form = QWidget()
        label_name = QLabel("Full name:")
        line_edit_name = QLineEdit()
        first_layout = QHBoxLayout()
        first_layout.addWidget(label_name)
        first_layout.addWidget(line_edit_name)
        widget_form.setLayout(first_layout)

        widget_button = QWidget()
        button_one = QPushButton("One")
        button_one.clicked.connect(self.button_clicked)
        button_two = QPushButton("Two")
        button_three = QPushButton("Three")
        buttons_layout = QVBoxLayout()
        buttons_layout.addWidget(button_one)
        buttons_layout.addWidget(button_two)
        buttons_layout.addWidget(button_three)
        widget_button.setLayout(buttons_layout)

        tab_itself.addTab(widget_form, "Name")
        tab_itself.addTab(widget_button, "Buttons")

        layout = QVBoxLayout()
        layout.addWidget(tab_itself)
        self.setLayout(layout)
        
    def button_clicked(self):
        pass


def main():
    app = QApplication(argv)
    window = tab_test()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()
