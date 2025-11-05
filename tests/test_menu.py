from PySide6.QtWidgets import QMainWindow, QToolBar, QStatusBar, QPushButton
from PySide6.QtCore import QSize

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
    
        self.setWindowTitle("MainWindow")

        # Functionality inherited from QMainWindow
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&File")
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit)

        edit_menu = menu_bar.addMenu("&Edit")

        edit_menu.addAction("Copy")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Paste")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")

        menu_bar.addMenu("&Window")
        menu_bar.addMenu("&Setting")
        menu_bar.addMenu("&Help")

        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)

        # action1 = QAction("Some Action", self)
        # action1.setStatusTip("Status message for some action")

        self.setStatusBar(QStatusBar(self))

        button1 = QPushButton("Button One")
        button1.clicked.connect(self.button1_clicked)
        self.setCentralWidget(button1)

        
    def button1_clicked(self):
        print("Button Clicked")

    def quit(self):
        self.app.quit()