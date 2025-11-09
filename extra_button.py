from PySide6.QtWidgets import QApplication, QWidget, QButtonGroup, QVBoxLayout, QGroupBox, QCheckBox, QHBoxLayout

class test_button(QWidget):
    def __init__(self):
        super().__init__()

        hmm = QGroupBox("Options")

        temp_sesh = QCheckBox("Sesh")
        temp_sesh.toggled.connect(self.custom_one)

        temp_ground = QCheckBox("Ground")
        temp_ground.toggled.connect(self.custom_two)

        group_layout = QVBoxLayout()
        group_layout.addWidget(temp_sesh)
        group_layout.addWidget(temp_ground)
        hmm.setLayout(group_layout)

        main_layout = QVBoxLayout()
        main_layout.addWidget(hmm)
        self.setLayout(main_layout)

    def custom_one(self, checked):
        if checked:
            print("checked")
        else:
            print("not checked")
        
    def custom_two(self, checked):
        if checked:
            print("checked")
        else:
            print("not checked")

def main():
    app = QApplication([])
    window = test_button()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()

