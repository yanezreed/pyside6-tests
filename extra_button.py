from PySide6.QtWidgets import QApplication, QWidget, QButtonGroup, QVBoxLayout, QGroupBox, QCheckBox, QHBoxLayout

#class test_button(QWidget):
#    def __init__(self):
#        super().__init__()
#
#        hmm = QGroupBox("Options")
#
#        temp_sesh = QCheckBox("Sesh")
#        temp_sesh.toggled.connect(self.custom_one)
#
#        temp_ground = QCheckBox("Ground")
#        temp_ground.toggled.connect(self.custom_two)
#
#        group_layout = QVBoxLayout()
#        group_layout.addWidget(temp_sesh)
#        group_layout.addWidget(temp_ground)
#        hmm.setLayout(group_layout)
#
#        main_layout = QVBoxLayout()
#        main_layout.addWidget(hmm)
#        self.setLayout(main_layout)
#
#    def custom_one(self, checked):
#        if checked:
#            print("checked")
#        else:
#            print("not checked")
        
#    def custom_two(self, checked):
#        if checked:
#            print("checked")
#        else:
#            print("not checked")

class excl_format(QWidget):
    def __init__(self):
        super().__init__()
        
        items = QGroupBox()
        item1 = QCheckBox("lego")
        item2 = QCheckBox("Doll")
        item3 = QCheckBox("Dogo")

        item_button = QButtonGroup(self)
        item_button.addButton(item1)
        item_button.addButton(item2)
        item_button.addButton(item3)
        item_button.setExclusive(True)

        item_layout = QVBoxLayout()
        item_layout.addWidget(item1)
        item_layout.addWidget(item2)
        item_layout.addWidget(item3)
        items.setLayout(item_layout)

        layout = QHBoxLayout()
        layout.addWidget(items)

        self.setLayout(layout)


def main():
    app = QApplication()
    window = excl_format()
    window.show()

    app.exec()

if __name__ == "__main__":
    main()

