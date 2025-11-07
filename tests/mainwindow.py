from PySide6.QtWidgets import QMainWindow, QToolBar, QPushButton, QStatusBar, QMessageBox
from tests.test_widget import TestWidget
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import QSize

class MainWindow(QMainWindow):
    # note, app is being passed into the class call
    def __init__(self, app):
        super().__init__()
        # Used to exit later on
        self.app = app

        self.setWindowTitle("Main Window")

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&File")
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit_method)

        edit_menu = menu_bar.addMenu("&Edit")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Paste")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")

        menu_bar.addMenu("&Window")
        menu_bar.addMenu("&Setting")
        menu_bar.addMenu("&Help")
        
        toolbar = QToolBar("Main Toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        action1 = QAction("Action", self)
        action1.setStatusTip("Status Message")
        action1.triggered.connect(self.toolbar_button_click)
        toolbar.addAction(action1)

        toolbar.addSeparator()
        toolbar.addWidget(QPushButton("Click here"))

        # action2 = QAction(QIcon("start.png"), "Action Two", self)
        # action2.setStatusTip("Status message for action two!")
        # action2.triggered.connect(self.toolbar_button_click)
        # action2.setCheckable(True)
        # toolbar.addAction(action2)

        self.setStatusBar(QStatusBar(self))


        test_widget = TestWidget()
        self.setCentralWidget(test_widget)
        self.resize(800, 600)

        # button1 = QPushButton("Test")
        # button1.clicked.connect(self.button_test)
        # self.setCentralWidget(button1)

        # button_critical = QPushButton("Critical")
        # button_critical.clicked.connect(self.button_clicked)
        # self.setCentralWidget(button_critical)


        # button_Warning = QPushButton("Warning")
        # button_Warning.clicked.connect(self.button_clicked)
        # self.setCentralWidget(button_Warning)


    def quit_method(self):
        self.app.quit()
    
    def toolbar_button_click(self):
        self.statusBar().showMessage("Something Happening", 3000)
    
    def button_test(self):
        pass

    # Creating message box
    # def button_clicked(self):
      #  message = QMessageBox()
      #  message.setMinimumSize(700,200)
      #  message.setWindowTitle("Message Title")
      #  message.setText("Something happened")
      #  message.setInformativeText("What would you prefer?")
      #  message.setIcon(QMessageBox.Critical)
      #  message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
      #  message.setDefaultButton(QMessageBox.Ok)
      #  ret = message.exec()
      #  if ret == QMessageBox.Ok:
      #      print("User chose Ok")
      #  else:
      #      print("User chose Cancel")