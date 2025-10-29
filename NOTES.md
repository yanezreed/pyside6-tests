installed: python, powershell, pyside6
(py 3.11.0 is the newest version that works with pyside6)

visual studio + is free, same layout cross operating system, familiar
installation steps:

● open terminal (powershell)
● "python" will show version/if installed
● "exit()"
● "pip3 install pyside6"
● install visual studio
● install python extension
● open empty folder in vs

---

"from PySide6.QtWidgets import QApplication, QWidget"
"import sys"
"app = QApplicaation(sys.argv)"

^^ object similar to flask ^^

produces a empty window when ran with "python main.py"
this is produced using python(3.11.0), pyside6, and vsc...

---

"PySide6.QtWidgets" refers to the submodule inside of the "PySide6" module

PySide6/
├── QtWidgets/ ← submodule for GUI widgets
├── QtCore/ ← core non-GUI functionality (signals, slots, etc.)
├── QtGui/ ← graphics, fonts, images, etc.
├── QtNetwork/ ← networking
└── ... ← other submodules

"sys.args" is passed into the class "QApplication()"
Qt uses these arguments for things like:

Parsing Qt-specific flags (e.g., -style, -platform, -reverse, etc.)
Setting the application name (if not explicitly set)
Handling high-DPI, styles, platforms, etc.

"QApplication" (app) is basically en capsuling all of your logic
by keeping the app running, processes clicks, keypresses, timers...
it parses qt-specific flags inputted via args (commands for qt)...
holds application identity ie name of company or app...
holds global settings like fonts, cursors and clipboards...
and all "QWidget" will live inside it similar to html structure...

---

window = QWidget()
window.show()

But behind the scenes, app is:

● Talking to Windows/macOS/Linux
● Managing mouse/keyboard input
● Redrawing the screen
● Handling close/minimize
● Running the infinite loop that keeps it alive

Note: "app.exec()" starts a while loop to keep the window in a event loop

---

"QWidget" receives mouse, keyboard and other events from the system...
parent widgets are called a window, and have a frame and title bar (which...
can also be edited using window flags)...
they accept two arguments on creation...
"QWidget \*parent = nullptr" where if the value is the null pointer, it will by default be a window
And it will also accept flags to alter its appearance and functionality

---

Note: calling "QMainWindow" in python will create a window (C++ is different)

"window.setCentralWidget(button)" is necessary here as
"QMainWindow" requires a special layout system including:
● A menu bar
● Toolbars
● A status bar
● And one central widget
When you call "setCentralWidget(widget)", you’re telling the "QMainWindow"
“This is the main widget that fills the central area of the window.”

---
