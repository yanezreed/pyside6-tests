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

note:

- here i'm creating a button within the "QMainWindow" setting it to the centre via "self."
- because the button is being set central, no other content is within the window
- the "app" should be thought as the script/brain, and the widgets/window is whats visable

* here i'm importing all the relevant classes into my new file "button_frame.py"
* i repeat the process of accessing "QMainWindow" functionality through initialization
* first initializing an object "init(self)" then accessing parents functionality through "super()"

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

note:

- "Pyside6.QtWidgets" is a modal within pyside6, giving us access to widgets
- "sys.argv" is used to pass commands to "QApplication"
- "app = QApplication()" is executed using "app.exec()"
- i should think of "QApplication" as the root of the tree (similar to html)
- all events, such as a button click are listened for by the "QApplication" object
- "app.exec()" is what catches an event when executed
- recorrection: "app.exec()" functions not as a while loop, but rather similar to my c http server
- by starting a "Qt event loop", blocks my python script and waits efficiently for system events
- ie. mouse clicks, key presses, network, timers...
- similar to my flask applications qt dispatches singals to the appropriate widget/object in my code
- with these widgets only running when triggered by an event (like slot functions)
- https://doc.qt.io/qt-6/qtwidgets-index.html

---

## Window details

note:

- by default widgets in pyside6 are "hidden"
- using "window = QWidget()" -> "window.show()" I can create/reveal a widget inside my "QApplication"
- structure; app("QMainWindow" "super()." -> "QPushButton" "self.setCentralWidget(button)")
- by using separate files,

## QMainWindow Class Documentation

note:

- "QMainWindow" provides the main ui framework
- includes built in areas for; "QMenuBar", "QToolBar", "QDockWidget" and "QStatusBar"
- "self.menuBar()" -> returns (and auto creates) the "QMenuBar"
- i can use "menuBar().addMenu("&Name")" -> to create and returns a "QMenu"
- add "QActions" to "QMenu" via "menu.addAction(action)"
- "setMenuBar()" is "not needed" in typical pyside6 apps

```python
class MainWindow(QMainWindow):
  def create_toolbar(self):
      toolbar = self.addToolBar("Main")
      toolbar.addAction("New")
      toolbar.addAction("Open")
      toolbar.addAction("Save")
```

![notes sixth sc]("assets\image-06.PNG")

---

## Structure Revisit

note:

- files split up into main/app, with "QApplication" being the conductor
- the other files are essentially called upon classes with specific roles
- "PySide6.QWidgets" (modual) -> "QMainWindow, QPushButton, QApplication"
- each new class/widget i encounter, i should be researching via the documentation
- to understand structure, purpose, and how it connects to the rest of the app
- ie. "QMainWindow" allows me the structure to encapsulate a widget

![notes seventh sc]("assets\image-07.PNG")

- `window.setCentralWidget(button)` - centres button within the windows structure
- `window.setWindowTitle(" ")` - inputs text within the title slot of "QMainWindow"
- `button.setText(" ")` - button being the object created by "QPushButton"
- "setText" is the inherited classes functionality being exploited

## Personal Notes

note:

- import classes to reduce complexity, inheriting and building upon widgets to fit
- i create physical widgets via objects initialized through instantiating a class
- this is done via `def __init__(self):` -> `super.__init__()`
- with "super." not ending with a ":" as im only importing the functionality...
- and afterwards i want to include my own code (similar to linking when compiling)
- by doing this, i can now access functionality from the parent/inherited class
- `self.setWindowTitle(" ")` can be used in a class called w/e i want

note:

- to create the physical object, i need to always initialize the object via class
- i then am able to access class specific methods through the use of the "." operator
- ie. `button.setText(" ")` uses the "QPushButton" method through the object

* lastly; i must ensure i only import the relevant modules/libraries into files
* as wasting resources via importing "QApplication" into every file is unacceptable

---

## Signals and slots

- are a mechanism qt provides to link events with executables within program ie.

* button-click/event (signal) -> executable section(s) of code (slot)

* `button = QPushButton(" ")` -> `button.clicked.connect(button_clicked)`
* ".clicked" being an method inside the object, triggered by the event...
* ".connect" being the action taken, executing the "(button_clicked)" method

## Experimentation

- again with the idea of separating any logic related to the button/window from main
- finding that by declaring the signal ".clicked.connect" within the imported class...
- i can then "import" both the object and its reactive functionality into main.py
- reducing complexity, and keeping all code related to the widget in one file

note: to know what events can be utilised as signals, i must consult documentation
usally however the actual signals can be found through "QtWidgets.QAbstractButton"
which is a parent class to "QtWidgets".

common signals include; `.clicked .pressed .released .toggled` (for checkable buttons)

![notes eight sc]("assets\image-08.PNG")

---

note:

- `.clicked` as a signal can also hold a value ie. "Flase" if not checked...
- `button.setCheckable(True)` firstly makes the "QPushButton" object checkable
- the checkable button will now toggle between two different states

```python
from PySide6.QtWidgets import QMainWindow, QSlider
from PySide6.QtCore import Qt

class SliderFrame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setTitle("Slider Frame")
        self.setCentralWidget(slider)

        # Creates a customized slider form QtCore

        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(0)
        slider.setMaximum(100)
        slider.setValue(25)

        # I need to remember to always call functions with `self`

        slider.valueChanged.connect(self.slider_data)

    def slider_data(self, data):
        print("slider moved to:", data)
```

note:

- here in a similar fashion i'm creating a slider with a signal/slot within the class
- `.valueChanged` being the signal, and is connected to the slot via `.connect`
- i need to remember to access all values/methods in the class using "self."

- `slider = QSlider(Qt.Horizontal)` produces a horizontal slider
- with "Qt.Horizontal" directing the slider to function left to right
- whenever the slider is changed, it will "signal" the updated value
- through; `valueChanged()`
- other signals it can emit; `sliderPressed()`, `sliderMoved()`, `sliderReleased()`

- by checking the documentation of `.valueChanged`, we can see that...
- "PySide6.QtWidgets.QAbstractSlider.valueChanged(value)" <--
- showing me that a value will be returned to the slot by the signal
- representing what current value the slider has been changed too

```python
def respond_to_slider(self, data):
  print("slider moved to: ", data)

# Main bulk code

slider.valueChanged.connect(respond_to_slider)
```

- so by connecting the signal `valueChanged` with the slot `respond_to_slider`
- by the very nature of the signal the sliders value is sent to my function
- lastly i need to keep in mind that `connect` takes the argument of the slot
- so i can manipulate what will execute when a certain signal is emitted

note:

- similar to the value returned by the slider signal and passed to the slot
- `button.setCheckable(True)` allocates the value true to the checked button
- unchecking said button will return "false" to my slot via `.connect()`
- meaning i am simply telling the button to keep track of the binary state
