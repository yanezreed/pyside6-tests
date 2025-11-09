from PySide6.QtWidgets import QApplication, QHBoxLayout, QWidget, QLabel, QLineEdit, QSizePolicy, QVBoxLayout, QPushButton

class sizePol(QWidget):
    def __init__(self):
        super().__init__()
        label = QLabel("Some text: ")
        line_edit = QLineEdit()
        # note; this is the typical behaviour of widgets
        line_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        layout = QHBoxLayout()
        layout.addWidget(label)
        layout.addWidget(line_edit)

        button_one = QPushButton("One")
        button_two = QPushButton("Two")
        button_three = QPushButton("Three")

        temp_layout = QHBoxLayout()
        temp_layout.addWidget(button_one, 2)
        temp_layout.addWidget(button_two, 1)
        temp_layout.addWidget(button_three, 1)

        final_layout = QVBoxLayout()
        final_layout.addLayout(layout)
        final_layout.addLayout(temp_layout)

        self.setLayout(final_layout)

def main():
    app = QApplication()
    window = sizePol()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()