# PySide6 Notes

installed:

1. python
2. powerShell
3. pySide6

   _(python 3.11.0 is the newest version that works with pyside6)_

note : vs note : vs for me is a great option; being free and similar layout,
regardless of the operating system (which could change later).

---

## Installation Steps

1. open terminal (powershell)
2. run `python` — this will show version/if installed
3. type `exit()`
4. run `pip3 install pyside6`
5. install visual studio
6. install the python extension
7. open an empty folder in vs

---

## Basic Example

![notes first sc](assets\image-01.png)

```python
from PySide6.QtWidgets import QApplication, QWidget
import sys

app = QApplication(sys.argv)
```

_(produces an empty window when ran with "python main.py")_

this is produced using:

1. Python 3.11.0
2. PySide6
3. Visual Studio Code (VSC)

---

## Pyside Widgets

"PySide6.QtWidgets" refers to the submodule inside of the pyside6 module

PySide6/
├── QtWidgets/ ← submodule for GUI widgets
├── QtCore/ ← core non-GUI functionality (signals, slots, etc.)
├── QtGui/ ← graphics, fonts, images, etc.
├── QtNetwork/ ← networking
└── ... ← other submodules

"sys.argv" is passed into the class "QApplication()"

qt uses these arguments for things like:

1. parsing qt-specific flags (e.g., -style, -platform, -reverse, etc.)
2. setting the application name (if not explicitly set)
3. handling high-dpi, styles, platforms, etc.

notes:

- "QApplication" (app) is basically encapsulating all logic for widgets
- keeping the app running, processes clicks, keypresses, timers...
- it parses qt-specific flags inputted via args (commands for qt)
- holds application identity ie. name of company or program...
- holds global settings such as fonts, cursors and clipboards
- all "QWidget" objects live inside it similar to html tree structure

---

## Pyside Running

```python
window = QWidget()
window.show()
```

behind the scenes, app is:

- talking to windows/macos/linux
- managing mouse/keyboard input
- redrawing the screen
- handling close/minimize
- running the infinite loop that keeps it alive

  _("app.exec()" starts a while loop to keep the window in an event loop)_

---

notes python, c++ (helping me understand via my c code knowledge):

- "QWidget" receives mouse, keyboard and other events from the system
- parent widgets are called a window, and have a frame and title bar
- (which can also be edited using window flags), they accept two arguments on creation
- "QWidget \*parent = nullptr" where if the value is the null pointer, it will by default be a window
- will also accept flags to alter its appearance and functionality

---

## Window Details

_(calling "QMainWindow" in python will create a window,C++ is different)_

![notes second sc](assets\image-02.png)

_("window.setCentralWidget(button)" is necessary here as)_

"QMainWindow" requires a special layout system including:

- a menu bar
- toolbars
- a status bar
- and one central widget

  _(when you call "setCentralWidget(widget)", you’re telling the "QMainWindow")_
  _(“this is the main widget that fills the central area of the window.”)_

---

## Revisiting Python Class/Subclass

![notes third sc](assets\image-03.PNG)

```python
class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        button = QPushButton("Click Me")
        self.setCentralWidget(button)
```

notes:

- a subclass of "QMainWindow" is created with "MyMainWindow" inheriting functionality
- with all "QMainWindow" built in features, by subclassing i am able to customize
- "def init(self)" alongside "super().init()" initializes a object produced by the class
- calling the inherited classes "init" function before i add functionality
- "self.setWindowTitle("My App")" does exactly that via calling functionality within "self"
- "button = QPushButton("Click Me")" exactly like before creates an object
- with "QPushButton" being another class/Qt-widget (and is a child widget to the window)
- "self.setCentralWidget(button)" is more pyside6 specific
- it sets the object/widget "button" to the 'special area' of a "QMainWindow"
- like i noted earlier there can only be one central widget
- for more detailed specifics on various widgets i need to keep referring to the documentation

---

## Pyside Structure

QApplication → QMainWindow → Central Widget (e.g. QWidget)
└── Layout (e.g. QVBoxLayout)
└── Child Widgets (buttons, labels, etc.)

Note:

- the code above is still not as... structured as it could be
- by importing my button class into "main.py" to then be set as "self.setCentralWidget()"
- i can use this method to avoid over complicating "main" improving readability

---

## Understanding Set-Up

![notes fourth sc]("C:\Users\yanez\Desktop\Workspace Folder\assets\image-04.PNG")

![notes fifth sc]("C:\Users\yanez\Desktop\Workspace Folder\assets\image-05.PNG")

```python
from PySide6.QtWidgets import QMainWindow, QPushButton

class ButtonFrame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Button Frame")
        button = QPushButton("Press Here")
        self.setCentralWidget(button)
```

- here i'm importing all the relevant classes into my new file "button_frame.py"
- i repeat the process of accessing "QMainWindow" functionality through initialization
- first initializing an object "init(self)" then accessing parents functionality through "super()"

note (rubber ducking process):
that unlike using a decorator i can just pass the parent class as a argument into the subclass,
using "super().init" gives me access to the process the parent class executes (initializes) when
creating its own objects.

meaning that when "init(self)" is used an object is initialized and can technically then use all
of the functionality/methods of the parent via "self."

but because i have included "super().init" im passing the values/functionality which are given to
the parent classes objects, with the difference being i now have the ability to include more and more
of code ie. more values "self.value = 2" or more functionality by adding methods in this new subclass
(which will have to be compatible with the combination of code given to the object from
both the subclass and parent class initialization)...
