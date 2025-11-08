from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PySide6.QtGui import QPixmap
class QLImage(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QLabel Image")

        image = QLabel()
        image.setPixmap(QPixmap("assets\test_run.PNG"))

        layout = QVBoxLayout()
        layout.addWidget(image)

        self.setLayout(layout)




def main():
    app = QApplication()
    window = QLImage()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()