from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit
from sys import argv

class TestHolder(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        label = QLabel("Fullname: ")
        self.line_edit = QLineEdit()
        self.text_holder_label = QLabel("")

        layout.addWidget(label)
        layout.addWidget(self.line_edit)
        layout.addWidget(self.text_holder_label)

        self.line_edit.textChanged.connect(self.text_change)

        self.line_edit.cursorPositionChanged.connect(self.cursor_position_changed)

        # Essentially do the same process
        self.line_edit.editingFinished.connect(self.editing_finished)
        self.line_edit.returnPressed.connect(self.return_pressed)

        self.line_edit.selectionChanged.connect(self.selection_changed)

        self.line_edit.textEdited.connect(self.text_edited)


    def button_clicked(self):
        print("Fullname: ", self.line_edit.text())
        self.text_holder_label.setText(self.line_edit.text)

    def text_change(self):
        self.text_holder_label.setText(self.line_edit.text())

    def cursor_position_changed(self, old, new):
        print("old cursor position: ", old, "-new cursor position:", new)
    
    def editing_finished(self):
        print("Editing finished")

    def return_pressed(self):
        print("Enter pressed")

    def selection_changed(self):
        print("Selection changed: ", self.line_edit.selectedText())

    def text_edited(self, new_text):
        print("Text edited, new text: ", new_text)
    

def main():
    app = QApplication()
    window = TestHolder()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()