from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QMessageBox

class TestWidget(QWidget):
    def __init__(self):
        super().__init__()

        # All contents will be held within inherited widget

        button_critical = QPushButton("Critical")
        button_critical.clicked.connect(self.button_critical)

        button_question = QPushButton("Question")
        button_question.clicked.connect(self.button_question)

        button_information = QPushButton("Information")
        button_information.clicked.connect(self.button_information)

        button_warning = QPushButton("Warning")
        button_warning.clicked.connect(self.button_warning)

        button_about = QPushButton("About")
        button_about.clicked.connect(self.button_about)
        
        layout = QVBoxLayout()

        layout.addWidget(button_critical)
        layout.addWidget(button_question)
        layout.addWidget(button_information)
        layout.addWidget(button_warning)
        layout.addWidget(button_about)
        self.setLayout(layout)
  
    def button_critical(self):
        message = QMessageBox()
        message.setMinimumSize(700,200)
        message.setWindowTitle("Message Title")
        message.setText("Something happened")
        message.setInformativeText("What would you prefer?")
        message.setIcon(QMessageBox.Critical)
        message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        message.setDefaultButton(QMessageBox.Ok)
        ret = message.exec()
        if ret == QMessageBox.Ok:
            print("User chose Ok")
        else:
            print("User chose Cancel")

    def button_question(self):
        message = QMessageBox()
        message.setMinimumSize(700,200)
        message.setWindowTitle("Message Title")
        message.setText("Something happened")
        message.setInformativeText("What would you prefer?")
        message.setIcon(QMessageBox.Question)
        message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        message.setDefaultButton(QMessageBox.Ok)
        ret = message.exec()
        if ret == QMessageBox.Ok:
            print("User chose Ok")
        else:
            print("User chose Cancel")

    def button_information(self):
        message = QMessageBox()
        message.setMinimumSize(700,200)
        message.setWindowTitle("Message Title")
        message.setText("Something happened")
        message.setInformativeText("What would you prefer?")
        message.setIcon(QMessageBox.Information)
        message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        message.setDefaultButton(QMessageBox.Ok)
        ret = message.exec()
        if ret == QMessageBox.Ok:
            print("User chose Ok")
        else:
            print("User chose Cancel")

    def button_warning(self):
        message = QMessageBox()
        message.setMinimumSize(700,200)
        message.setWindowTitle("Message Title")
        message.setText("Something happened")
        message.setInformativeText("What would you prefer?")
        message.setIcon(QMessageBox.Warning)
        message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        message.setDefaultButton(QMessageBox.Ok)
        ret = message.exec()
        if ret == QMessageBox.Ok:
            print("User chose Ok")
        else:
            print("User chose Cancel")

    def button_about(self):
        message = QMessageBox()
        message.setMinimumSize(700,200)
        message.setWindowTitle("Message Title")
        message.setText("Something happened")
        message.setInformativeText("What would you prefer?")
        message.setIcon(QMessageBox.Warning)
        message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        message.setDefaultButton(QMessageBox.Ok)
        ret = message.exec()
        if ret == QMessageBox.Ok:
            print("User chose Ok")
        else:
            print("User chose Cancel")
    