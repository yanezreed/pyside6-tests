from PySide6.QtWidgets import QApplication, QWidget, QListWidget, QAbstractItemView, QVBoxLayout, QPushButton
from sys import argv

class test_list(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test List")

        self.list_widget = QListWidget(self)
        self.list_widget.setSelectionMode(QAbstractItemView.MultiSelection)
        self.list_widget.addItem("Soda")
        self.list_widget.addItems(["Coke", "Pepsi"])

        self.list_widget.currentItemChanged.connect(self.item_changed)
        self.list_widget.currentTextChanged.connect(self.text_changed)

        # Buttons

        add_item = QPushButton("Add Item")
        add_item.clicked.connect(self.add_item_function)

        delete_item = QPushButton("Delete Item")
        delete_item.clicked.connect(self.delete_item_function)

        item_count = QPushButton("Item Count")
        item_count.clicked.connect(self.item_count_function)

        selected_items = QPushButton("Selected Items")
        selected_items.clicked.connect(self.selected_items_function)

        layout = QVBoxLayout()
        layout.addWidget(self.list_widget)
        layout.addWidget(add_item)
        layout.addWidget(delete_item)
        layout.addWidget(item_count)
        layout.addWidget(selected_items)

        self.setLayout(layout)

    def item_changed(self, item):
        print(f"Current item: {item.text()}")

    def text_changed(self, text):
        print("Text changed: ", text)
        
    # Button methods

    def add_item_function(self):
        self.list_widget.addItem("New Item")

    def item_count_function(self):
        print("Item count:", self.list_widget.count())

    def delete_item_function(self):
        self.list_widget.takeItem(self.list_widget.currentRow())

    def selected_items_function(self):
        list = self.list_widget.selectedItems()
        for i in list:
            print(i.text())

def main():
    app = QApplication(argv)
    window = test_list()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()
