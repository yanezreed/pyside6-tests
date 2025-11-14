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

![notes first sc](assets\image-01.PNG)

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

![notes second sc](assets\image-02.PNG)

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

note: to know what events can be utilised as signals, i must consult documentation<br>
usually however the actual signals can be found through "QtWidgets.QAbstractButton"<br>
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
- representing what current value the slider has been changed to...

* ie. 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7... it will trigger a response each value

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

---

## QWidgets

- widgets are the basic components used to create the ui using qt
- all found in the "QWidgets" module

when you inherit "QWidget" into your class, you gain:

- your class becomes a visible widget that can be shown, hidden, resized, etc
- can override "paintEvent()" using "QPainter to draw custom graphics

- in terms of event handling, which is when a widget receives a message...
- when an event occurs ie. mouse-click, key pressed, window resized

```python
def mousePressEvent(self, event):
    print(f"Mouse clicked at: {event.pos()}")
```

- my widget/class can hold other widgets through "layout managers"
- lastly if my widget has children, they are auto deleted when the parent is

## QWidget Layout

notes:

1. `self.setWindowTitle` used to import a tab-like title for the window
2. buttons + signals/slots are created (giving them functionality)
3. to actually locate the widgets onto my `QWidget` (inherited) i need to add my widgets to a `QV(or H)BoxLayout` (any sort of layout) and apply this layout to the `QWidget` using `self.setlayout(this_layout)`<br>
4. lastly i can create methods/slots to react to my events

```python

from PySide6.QtWidgets import QPushButton, QWidget, QVBoxLayout

class RockWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rock Widget")

        initial_button = QPushButton("B1")
        initial_button.clicked.connect(self.functionOne)

        second_button = QPushButton("B2")
        second_button.clicked.connect(self.functionTwo)

      # Example of `horizontal` layout below
      # widget_layout = QHBoxLayout()
        widget_layout = QVBoxLayout()

        widget_layout.addWidget(initial_button)
        widget_layout.addWidget(second_button)

      # `widget_layout` now holds both buttons
        self.setlayout(widget_layout)


    def functionOne(self):
        pass

    def functionTwo(self):
        pass
```

additional notes:

- must remember that `QWidget` needs a layout to set widgets
- as it requires structure to place the widgets where they need to be!<br>

- ie. `QHBoxLayout` orders the widgets top to bottom (vertically)
- and `QVBoxLayout` orders the widgets right to left (horizontally)<br>

* `self.setlayout()` then sets the given layout (added as an argument)
* as the widgets layout manager, controlling the placement of its child widgets<br>

* note: `self.setlayout()` is a method of the `QWidget` class

---

```python
from PySide6.QtWidgets import QSlider, QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt

class RockWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rock Widget")

        self.label = QLabel("Height & Width")

        self.initial_sli = QSlider(Qt.Horizontal)
      # valueChanged signal insteaad of clicked here
        self.initial_sli.sliderReleased.connect(self.functionOne)
        self.initial_sli.setMinimum(0)
        self.initial_sli.setMaximum(100)
        self.initial_sli.setValue(25)

        self.second_sli = QSlider(Qt.Horizontal)
        self.second_sli.sliderReleased.connect(self.functionTwo)
        self.second_sli.setMinimum(0)
        self.second_sli.setMaximum(100)
        self.second_sli.setValue(25)

      # Example of `horizontal` layout below
      # widget_layout = QHBoxLayout()
        widget_layout = QVBoxLayout()

        widget_layout.addWidget(self.label)
        widget_layout.addWidget(self.initial_sli)
        widget_layout.addWidget(self.second_sli)

        self.setLayout(widget_layout)


    def functionOne(self):
        hdata = self.initial_sli.value()
        print(f"Height = {hdata}")

    def functionTwo(self):
        wdata = self.second_sli.value()
        print(f"Width = {wdata}")
```

## SliderRealeased Experiment

notes:

- by using the `self.` before creating the slider in my class
- im effectively inheriting the classes attributes to my own class/object
- meaning on a event such as `sliderReleased` which is a signal for the slider class
- in my slot/function, by accessing `self` i am able to go into that objects value
- `self.initial_sli.value()` to access that value, to then use it however i may

---

## QMainWindow Class

- gives me access to a layout including; menus, toolbars, status bars and actions
- these components reside at predetermined locations on the layout
- to build on `QMainWindow` i will create a class, inheriting its functionality

```python
from PySide6.QtWidgets import QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
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
```

notes:

- diving into how i can set up a menu-bar

1. `menu_bar = self.menuBar()` taps into the inherited class to create a menu object
2. `file_menu = menu_bar.addMenu("&File")` similarly allows me to create a file menu
   which can be seen through examples such as photoshop, word or chrome...
   this is achieved by tapping into the menu/objects functionality calling `add.menu`
   and passing in the argument `(&File)`, producing a new object `file_menu`
3. for `quit_action = file_menu.addAction(self.quit)` a `QAction` is created...
   when the action is triggered, because it has been created with `.addaction` and...
   the provided callable `self.quit` when the action is clicked the method is called

- note: `QAction` is an object where it can be triggered by multiple ways -> method

4. ie. `quit_action.triggered.connect(self.quit)` is put in place to connect the
   object/"QAction" with the slot/method via the use of `.triggered`
5. i then am adding extra actions, via the use of `.addAction` keyword
   these actions are inside the "edit" file in the menu, accessed via the object
6. lastly im adding extra files to the `menu_bar` itself

```python
    toolbar = QToolBar("My main toolbar")
    toolbar.setIconSize(QSize(16,16))
    self.addToolBar(toolbar)
```

note:

- `toolbar = QToolBar` allows me to create a object
- `.setIconSize()` allows me to go inside the object and customize it
- using `self.addToolBar(toolbar)` im adding what ive created above to `QMainWindow`

---

```python
class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        # Used to exit later on
        self.app = app

        self.setWindowTitle("Main Window")

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&File")
```

note:

- reminder; `.menuBar` is one of many functions in `QMainWindow`
- these are always accessed through the use of `self.`
- as the object/class is inheriting `QMainWindow`
- the class is an extension of itself, with extra functionality

Now we have a menu with a "File" option but with nothing inside of it

note:

- `.addAction("Anything")` allows me to add options to the `file_menu` object
- reminder; `file_menu = menu_bar` + `.addMenu("&File")` creates the object

```python
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&File")
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit_method)

    def quit_method(self):
        self.app.quit()
```

note:

1. `menu_bar` is created (the actual widget menu bar)
2. `file_menu` is created by adding `&File` to the `menu_bar` itself
3. `quit_action` is the QAction object created by adding the option "Quit" to the `&File`
4. the QAction is used to connect via the signal `triggered` to my method
5. `self.app.quit()` closes app

---

## Toolbar

```python
        toolbar = QToolBar("Main Toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)
```

1. toolbar created, i can now aadd actions, widgets and separators...
2. `QSize` used to determine size in locked location in `QMainWindow` layout
3. `self.addToolBar(toolbar)` adds the widget to the main window

```python
        action1 = QAction("Action", self)
        action1.setStatusTip("Status Message")
        action1.triggered.connect(self.toolbar_button_click)
        toolbar.addAction(action1)
```

4. creates a QAction object, which is a user invokable command

- it appears as a label/text for the user (in this case within the tool bar)
- takes a second argument of "self", so the action is owned by the window
- which is extremely important as it means the action will be cleaned along with the parent

5. `action1.setStatusTip("Status Message")` sets a status tip for the action
6. next; i create a signal `triggered` to a slot `self.toolbar_button_click`
7. adds the action instance to the toolbar as a clickable item

```python
    def toolbar_button_click(self):
        print("Triggered")
```

- next im again adding a QAction to my toolbar, but this time in the form of an icon not text

8. using `action2 = QAction(QIcon("start.png"), "Action Two", self)`, with three arguments

- the first argument, loads an image file to the toolbar button (visual for user)

* the second gives a text label along side the icon
* the third `self` ensures the widget is cleaned up alongside the parent

9. `action2.setStatusTip("Status message for action two!")` again sets a status tip (when hovered)
10. `action2` here is set a signal/slot, connecting to `self.` + method when triggered
11. `action2.setCheckable(True)` makes the action checkable

- which effectively turning the button into a toggle (boolean)
- slots/methods can query the state of the button via

```python
def toolbar_button_click(self, checked):
    print("Checked:", checked)
```

12. lastly `toolbar.addAction(action2)` sets the action to the toolbar

- extra note; if i want to see what signals can be used for each action, i need to check the docs
- ie. "QAction docs", will also show signal parameters in/out

```python
        toolbar.addSeparator()
        toolbar.addWidget(QPushButton("Click here"))
```

- i am also able to add a separator for the tool bar and include other widgets
- these objects/methods are all accessed via the tool bar object/class

---

## Status bar

```python
        self.setStatusBar(QStatusBar(self))

    def toolbar_button_click(self):
        self.statusBar().showMessage("Something Happening", 3000)
```

notes:

- here i am creating a status bar through the use of the class `QMainWindow`
- the bar is created via a method as there is a dedicated location for the widget within its layout
- ie. status bar lives at the bottom left of the MainWindow
- is designed to give brief updates/hints (ready, saving file)...

- when a method is triggered via any means
- i can access the status bar widget via `self.` and command it to display a message
- a string and a time limit are taken as arguments (3000 milliseconds here)

---

- note: items which have a dedicated location on QMainWindows layout are all called via `self.`
- other widgets on the other hand are called through imported classes
- these widgets are then set to locations on the QMainWindow or will not be show
- ie.

```python
        button1 = QPushButton("Test")
        button1.clicked.connect(self.button_test)
        self.setCentralWidget(button1)
```

![notes nine sc]("assets\image-09.PNG")

---

## QMessageBox

- is a class i can use to set up temporary messages boxes for the user
- which can contain QPushButtons (ie. "ok", "cancel")

```python
    def button_clicked(self):
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
```

notes:

1. method is defined, within the MainWindow class, will be ran via connection
2. `QMessageBox()` object created
3. minimum size set in pixels
4. title is set + primary text within the box `message.setText("")`
5. `message.setInformativeText("")` simply adds a secondary line
6. `message.setIcon(QMessageBox.Critical)` -

- sets an icon for the message box; ie. `Information`, `Warning`, `Critical` or `Question`

7. `message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)` adds buttons + text
8. `message.setDefaultButton(QMessageBox.Ok)` allows me to select a default button, via "."

9. `ret = message.exec()` displays the message box, pausing execution until the user clicks an option
10. depending on the option chosen, "QMessage.PickedOption" is returned and passed to the code below
11. once an option is selected the chosen path is executed... (note "ret" short for return)...

```python
        button_critical = QPushButton("Critical")
        button_critical.clicked.connect(self.button_clicked)
        self.setCentralWidget(button_critical)
```

- to display the message box to the user i can connect it via a push button

---

## QVBoxLayout

note:

- to display all of these buttons i might want to hold them within a widget
- by making a new file, class and inheriting QWidget functionality
- i will be able to import the entire thing as a module

- importantly i will need a layout to accommodate these buttons correctly
- a good design choice would be to hold them within a `QVBoxLayout`

```python
        layout = QVBoxLayout()

        layout.addWidget(button_critical)
        layout.addWidget(button_question)
        layout.addWidget(button_information)
        layout.addWidget(button_warning)
        layout.addWidget(button_about)

        self.setLayout(layout)
```

1. i first create a object from the chosen layout class
2. buttons are created through widgets, via the layout class methods
3. selecting `QWidget` via `self.` im able to set the layout to the widget

note: by doing this there is no need to individually assign push buttons to central widget

```python
        button_critical = QPushButton("Critical")
        button_critical.clicked.connect(self.button_critical)
```

- this is all thats needed, as they are added to the `QVBoxLayout`
- my entire self created class (with QWidget as a parent class), to my main file
- meaning all buttons and functionality will be imported as one

```python
        test_widget = TestWidget()
        self.setCentralWidget(test_widget)
        self.resize(800, 600)
```

1. after creating methods for each of my buttons (explained above)
2. i can now import this class into w/e file i want
3. in this example i am importing it to my `QMainWindow` class
4. using my `QWidget` class i should create a object
5. then setting said object to the parents layout, again using `self`
6. from here i can edit it it further as an object

```python
def button_critical(self):
    ret = QMessageBox.critical(
        self,
        "Message Title",
        "Something happened\n\nWhat would you prefer?",
        QMessageBox.Ok | QMessageBox.Cancel,
        QMessageBox.Ok
    )
    print("User chose Ok" if ret == QMessageBox.Ok else "User chose Cancel")
```

note: above is the short hand way to create methods, but does exactly the same thing

---

## QPushButton Signals Indepth

- `clicked`, `presses`, and `released` are all common signals used to connect to slots
- pressed & released are key when designing drawing applications...
- `toggled` is related to `clicked`([checked=false])
- as it is triggered whenever the state of the button is changed within the program
- note; the button needs to be set as a "checkable" before hand, for this to work

- testing the order of events in terms of signals on an individual button
- i found the order to be; pressed -> released -> clicked

![notes tenth sc]("assets\image-10.PNG")

- meaning `clicked` is only confirmed after both pressed + released have completed

## QLabel and QLineEdit

- allows me to create a section where the user can write a single line of text, `QLineEdit`
- `QLabel` allows me to include text beside it to structure my ui

![notes eleventh sc]("assets\image-11.PNG")

```python
        self.setLayout(QHBoxLayout)

        label = QLabel("Fullname: ")
        self.line_edit = QLineEdit()
```

- setting these widgets/objects up is easy, via there imported classes

```python
    self.line_edit.textChanged.connect(self.text_changed)
```

- by setting `QLineEdit` to the widget `self`
- when the `textChanged` i can connect the signal to my method/slot

- This is a signal emitted by QLineEdit whenever the text cursor position changes
- ie. when the user moves the cursor with arrow keys, clicks the mouse inside the field
- or even edits the text inside the box...
- note; again all of these signals are coded in the class `QLineEdit` and are also emitted

```python
    self.line_edit.editingFinished.connect(self.editing_finished)
    self.line_edit.returnPressed.connect(self.return_pressed)
```

- `editingFinished` simply means, when the user presses "enter"
- `returnPressed` is exactly the same...

```python
    self.line_edit.selectionChanged.connect(self.selection_changed)
```

- again a signal is emitted whenever the "text selection" changes
- ie. user selects text with mouse or keyboard
- the selection of text is cleared (e.g clicking elsewhere or moving the cursor)

- unlike `cursorPositionChanged` the signal does not carry arguments
- it will only notify the user when something has changed, nothing more

```python
    self.line_edit.textEdited.connect(self.text_edited)
```

- lastly this `QLineEdit` signal emits when the text is altered
- this could be through typing, pasting or deleting

---

## QLineEdit Connections

```python
    def button_clicked(self):
        print("Fullname: ", self.line_edit.text())

        self.text_holder_label.setText(self.line_edit.text)
```

- allows me to grab the text within the `QLineEdit` via its objects `.text` method
- secondly i can access a widget within the `QWidget` via `self`...
- using `.setText` and the argument of `.text` within another `self` object
- i can transfer the `.text` value across

```python
    self.line_edit.cursorPositionChanged.connect(self.cursor_position_changed)

    def cursor_position_changed(self, old, new):
        print("old cursor position: ", old, "-new cursor position:", new)
```

- `cursorPositionChanged` signal, carries two arguments to the slot
- the old position of the cursor and the new, each time it is moved/triggered

```python
    self.line_edit.editingFinished.connect(self.editing_finished)

    def editing_finished(self):
        print("Editing finished")
```

- quite simply when "enter" or clicks elsewhere/tabs out, a signal is emitted
- what ever code at the slot is executed, `returnPressed` is only "enter" activated

```python
    self.line_edit.selectionChanged.connect(self.selection_changed)

    def selection_changed(self):
        print("Selection changed: ", self.line_edit.selectedText())
```

- `selectionChanged` is triggered w/e the user changes text selection inside `QLineEdit`
- triggered by the user selecting some text
- or through moving the cursor to select a different portion of the text
- each time a signal is emitted, the currently selected substring inside the widget
- is available through the `QLineEdit` method `.selectedText()`
- if nothing is selected, the method returns an empty string -> ""

```python
    self.line_edit.textEdited.connect(self.text_edited)

    def text_edited(self, new_text):
        print("Text edited, new text: ", new_text)
```

- `textEdited` signal sends one argument to the slot
- it is triggered/emitted only when the user manually edits the text
- again via typing, deleting or pasting in the field...
- each time the value is changed within the box, the value itself is sent as an argument
- meaning the slot will receive the text as it is being written or deleted

---

## Second Look At Layout

```python
        layout = QVBoxLayout()
        self.setLayout(layout)

        label = QLabel("Fullname: ")
        self.line_edit = QLineEdit()
        self.text_holder_label =

        layout.addWidget(label)
        layout.addWidget(self.line_edit)
        layout.addWidget(self.text_holder_label)
```

1. i create an object using the imported class of `QVBoxLayout` (or H)...
2. accessing `QWidget` via `self`, i set its layout to my objects value `QVBoxLayout`
3. i create a `QLabel` object, which is simply a line of text
4. accessing `QWidget` again, im storing `QLineEdit` within `self`

- remember that this is done in the same way as i would store a int value
- ie. `self.value` = 13, `QWidget` simply stores the value to be accessed through it
- note; it is an object created by `QLineEdit` not the code of the class
- effectively the widget/lineedit box is being held

5. again, `QWidget` is accessed to store the object of the widget class `QLabel`

6) this time the `layout` object is accessed which itself is being stored within `QLabel`
7) all three objects are now stored within the layout object inside the `QWidget`

note:

- by first storing `QLineEdit()` and `QLabel("")` within the `QWidget` or `self`
- we are able to always access these widgets later on to add customization...
- ie. while `layout.addWidget(label)` is clear/readable
- later on i will be unable to access `label` as a widget, as while it is still stored
- `layout` stores widgets/variables by reference rather than value
- meaning the code can be accessed but not altered after assignment

---

## QLineEdit Other Signals

- `cursorPositionChanged` as we know includes two cursor values; int oldPos and newPos...
- `editingFinished` emitted when widget loses focus after text was modified
- `inputRejected` emitted when input is rejected due to validator, used to error msg user
- `returnPassed` emitted when "enter" or "return" while widget in focus
- `selectionChanged` emitted when highlighted text changes, useful for copy buttons...
- `textChanged` includes one value; str text, holding the current value after any iteration
- `textEdited` is exactly the same bar it will not react to programmatic changes
- extra note; meaning if `setText` is executed on the widget, unlike `textChanged`
- the signal will not be triggered and a new string will not be emitted to the slot

## Layout Note

- when designing my pages, i can layer horizontal and vertical layouts on top of each other

```python

    h_layout = QHBoxLayout()
    h_layout.addWidget(label)
    h_layout.addWidget(self.line_edit)

    v_layout = QVBoxLayout()
    v_layout.addLayout(h_layout)
    v_layout.addWidget(button)
    v_layout.addWidget(self.text_holder_label)

    self.setLayout(v_layout)
```

- the key to this structure being line five
- as im adding `.addLayout(h_layout)` to my vertical layout, stacking my horizontal layout

## Self Reminder

- im creating a layout
- filling the page with widgets produced by imported classes
- i can use signals from these widgets to call slots/methods
- i can access values/variables from my widgets within my methods to achieve a desired effect
- ie. if button clicked -> slot: print "name: " + `self.line_edit.text()` (accessing object)

---

## QTextEdit

- `QTextEdit` offers large scale text box rather than one single line
- offering capabilities such as copy, cut, paste, undo, redo, set plaintext, set html and clear

```python
    self.text_edit = QTextEdit()
    self.text_edit.textChanged.connect(self.text_changed)

    copy_button = QPushButton("Copy")
    copy_button.clicked.connect(self.text_edit.copy)
```

- one key benefit to `QTextEdit` is that there are many pre-made slots for these functions
- ie. `self.text_edit.copy` allows me to access the widget and then the `.copy` slot

note:

- `self.text_edit = QTextEdit()` by storing the object in the class, i have access throughout
- allowing me to first trigger widgets `copy_button.clicked.connect(self.text_edit.cut)`
- then calling not my own slots, but premade -> `self.text_edit.cut`
- importantly accessing this functionality through the object created by `QTextEdit`
- meaning whatever is needed from the premade slot, will be accessible via the widgets values

```python
    h_layout = QHBoxLayout()
    h_layout.addWidget(copy_button)
    h_layout.addWidget(cut_button)
    h_layout.addWidget(paste_button)
    h_layout.addWidget(undo_button)
    h_layout.addWidget(redo_button)
    h_layout.addWidget(set_plain_text_button)
    h_layout.addWidget(set_html_button)
    h_layout.addWidget(clear_button)

    v_layout = QVBoxLayout()
    v_layout.addLayout(h_layout)
    v_layout.addWidget(self.text_edit)

    self.setLayout(v_layout)
```

- layout wise, in this example im choosing to do the same again
- by creating a horizontal layout for the buttons, i can then add this object to `QVBoxLayout`
- setting this layered structure as the layout of the `QWidget` itself

## Plain Text, HTML

- unlike the other widgets i have used so far `QLineEdit` does not have a `.text()` method
- as its designed to hold "rich text" which differs to plain text in many ways
- being able to hold text + embedded formatting instructions ie. styles, fonts, colours and images
- being held as html or markdown rather that a `.txt` file
- (not held as a string in storage, rather a tree of nodes)...

- so when accessed via the `.toPlainText()` method, all detail is lost in the conversion
- alternatively `.toHtml()` can display/format html or plane text values
- ie. plain text might output `<p style="margin-top:0; margin-bottom:0;">Hello</p>`
- and if the input is "rich text", it can be passed without alteration to other parts of my program

- summary; both of these `.to` methods are used to grab text from a widget in either type of format
- `QTextEdit` has alot of methods and signals detailed out in the documentation for future programs!

---

## Qlabel & Images

- using `QLabel` again, i have the ability to display images
- the image itself is required to be converted by the `QPixmap` function...
- and stored as a pixel map within the label object
- note; `QPixmap` is stored in the `PySide6.QtGui` module

```python
    image = QLabel()
    image.setPixmap(QPixmap("assets\test_run.PNG"))

    layout = QVBoxLayout()
    layout.addWidget(image)

    self.setLayout(layout)
```

---

## Size Policies (& Stretches)

- size policy is a property you can apply to your widgets that
- determines their behaviour when the user interface grows/shrinks
- ie. if the window grows, what do the widgets do themselves?

- stretch as a concept is a property that defines how many units each widget will occupy in a layout
- ie. one button may be given twice the width of another (and this is done via a stretch)
- these stretch proportions are held no matter how the window is altered...

```python
    line_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
```

- above is an example of accessing the `setSizePolicy` of my widget, in this case a `QLineEdit` object
- and adding two arguments to `setSizePolicy`, altering the objects behaviour when the widget is stretched
- the first argument details how i want the object to react horizontally via either `fixed` or `expanding`
- the second argument details how i want the object to react vertically

- note; by default my widgets will not expand

* if i was to set my "line edits" vertical behaviour to `expanding`
* the widget will inturn attempt to take up as much space in the layout as possible

## Stretches Specifically

- note; while "size policies" dictate how the object behaves, stretches dictate relative size
- stretches are applied through the `addWidget()` method, originating from some sort of `Q..Layout()` object

```python
    button_one = QPushButton("One")
    button_two = QPushButton("Two")
    button_three = QPushButton("Three")

    temp_layout = QHBoxLayout()
    temp_layout.addWidget(button_one, 2)
    temp_layout.addWidget(button_two, 1)
    temp_layout.addWidget(button_three, 1)
```

- note; without this intervention widgets will attempt to obtain an equal amount of space within the layout
- (this may not be apparent until the window is stretched, as orginally the widgets will be at default size)

---

## Grid Layout

- grid layouts in pyside6 all me to build structures like i have previously when using html tags
- here though, i am able to layout qtwidgets in a grid
- with the top left box, having an index of (0,0)
- we use indexes to determine where we want to position widgets in the grid layout
- note; in a similar way to how we allocated `stretch` to widgets...
- we can apply `rowSpan` or `columnSpan` to allow widgets to take up multiple index spots within the layout

```python
    grid_layout.addWidget(button_1,0,0)
    grid_layout.addWidget(button_2,0,1,1,2)
```

- note; here button one will live at index (0,0) on the grid
- button two, originates aaat (0,1), with the extra numbers identifying the column span and row span...
- with the first two digits representing the location/origin of the widget
- the next two after, detail the span row/column
- ie. here the widget has a height of "1" and will extend a column to have the size of "2"

note:

- both `setSizePolicy` and `stretch` can be used in combination to have full control of the widget
- even if the window is pulled out by the user or the size of the interface
- here by using the `Expanding` option, the button will grow with windows size

```python
    button_3.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
```

note:

- it is better i test layouts and how they will react to window shapes/sizes, ensuring they react how i want
- from here im able to now create signals/slots on the class objects (widgets)...

---

## QCheckBox & QRadioButton

- "checkboxes" like in html allow the user to select/deselect as many options/boxes as they please
- "radio buttons" however allow for one selected option maximum

- to be able to group buttons within the system, by their type (ie. radio buttons)
- i need to use the `QGroupBox` class
- a layout i needed within the `QGroupBox` to organise the widgets inside (ie. `QHBoxLayout`)

- the buttons/objects can now be created via the class `QCheckBox`
- connected via `widget.toggled.connect(self.object_function)` which will allow them to be checked

```python
def object_function(self, checked):
    if(checked):
        print("is checked")
    else:
        print("not checked")
```

- once the buttons are defined, i can add them to my layout via `.addWidget(button_one)`
- ie. `layout = QVBoxLayout()` -> `layout.addWidget(button_one)`
- then this layout is added to the `QGroupBox` object via `.setLayout`
- creating an organised layout of buttons inside the `QGroupBox` object
- so layout; `window` -> `QGroupBox` -> `QVBoxLayout` -> `QCheckBox`
- lastly note that `QGroupBox` is a widget not a layout object, meaning requires;

```python
        main_layout = QVBoxLayout()
        main_layout.addWidget(QGroupBox_object)
        self.setLayout(main_layout)
```

- i now have a window with an organised `QGroupBox` with checkable buttons
- which when selected connect with their slots and print an outcome to the terminal
- note; other signals include `clicked`, `pressed` and `released`

## Radio Buttons

note:

- the difference between "checkboxes" and "radiobuttons" is determined at grouping
- by using `QButtonGroup(self)` <- (requires the parent argument)
- the radio buttons are then declared via `.addButton()` on the `QButtonGroup(self)`
- including the `group.setExclusive(True)` to confirm this characteristic

note:
the difference between `QGroupBox` and `QButtonGroup` is that button group visually
does not effect the widgets or give them a layout, however it does in fact
logically group them together along with the instruction `group.setExclusive(True)`

```python
    group = QButtonGroup(self)
    group.addButton(1)
    group.addButton(2)
    group.addButton(3)
    group.setExclusive(True)
```

- once logically the buttons are grouped together
- i can create a layout ie. `QVBoxLayout` and use `.addWidget` again to organise

1. create a `QGroupBox`
2. create a `QVBoxLayout` layout
3. create the individual buttons ie. `QCheckBox`
4. add them to the layout `layout.addWidget()`
5. create a `QButtonGroup` to logically link the items
6. add a `.setExclusive(True)` instruction

note:

- to set up "radio buttons" is the same process, `.setExclusive(True)` is not needed
- using instead the class `QRadioButton` to create the objects/widgets
- again using the `QGroupBox` class to group the items logically before hand

---

## QListWidget

- allows the user to produce a list within the interface, with functionality;
- adding items, removing items, grab item count, select items, printing selected items

1. `self.list = QListWidget(self)` is used to create a list object within the parent
2. `self.list.setSelectionMode(QAbstractItemView.MultSelection)`

- via the object of `QListWidget` we can set the selective mode, multi/single selection
- `setSelectionMode` is necessary, along with the `QAbstractItemView` class + method

3. accessing my created `QListWidget` i can now add items:

```python
    self.list_widget = QListWidget(self)
    self.list_widget.setSelectionMode(QAbstractItemView.MultiSelection)
    self.list_widget.addItem("Soda")
    self.list_widget.addItems(["Coke", "Pepsi"])
```

- note; i can either use the `add.item` method to add a single item
- or i can use `addItems` which instead requires a list

4. i can now create a layout for my window (which will hold the list) ie.

```python
        layout = QVBoxLayout()
        layout.addWidget(self.list_widget)

        self.setLayout(self.layout)
```

- note; a layout if first created before the widget is added and both set to main

5. now we are able to utilize `QListWidget` signals that include;

- `currentItemChanged(currentItem)`, `currentRowChanged(currentRow)`
- `currentTextChanged`, `itemActivated(item)`, `itemChanged`, `itemClicked`
- `itemDoubleClicked`, `itemEntered`, `itemPressed`, `itemSelectionChanged`

```python
    self.list_widget.currentChanged.connect(self.item_changed)
```

- here i am able to pass the "current item" being changed by the user, to my slot

```python
    def item_changed(self, item):
        print(f"Current item: {item.text()}")
```

- item itself is a object, to display the items text i must access its value inside
- `currentTextChanged` can also be used to display text to the user...

```python
    self.list_widget.currentTextChanged.connect(self.text_changed)

    def text_changed(self, text):
        print("Text changed: ", text)
```

## QListWidget Buttons

- i now want to add buttons to allow user actions on my list widget/values

```python
        add_item = QPushButton("Add Item")
        add_item.clicked.connect(self.add_item_function)

        delete_item = QPushButton("Delete Item")
        delete_item.clicked.connect(self.delete_item_function)

        item_count = QPushButton("Item Count")
        item_count.clicked.connect(self.item_count_function)

        selected_items = QPushButton("Selected Items")
        selected_items.clicked.connect(self.selected_items_function)
```

- again im using a clicked signal to trigger my slots

```python
    def add_item_function(self):
        self.list_widget.addItem("New Item")
```

- using premade functions to allow easy functionality...
- by accessing the `QListWidget` i created, i can `addItem` to the list

```python
    def item_count_function(self):
        print("Item count: ", self.list_widget.count())
```

- again via my list i can access its `.count()` printing it to the terminal

```python
    def delete_item_function(self):
        self.list_widget.takeItem(self.list_widget.currentRow())
```

- allows me to `takeItem` from the list, on the `.currentRow()` of the list object
- note; always remember that passing `self` is how im able to access these values

```python
    def selected_items_function(self):
        list = self.list_widget.selectedItems()
        for i in list:
            print(i.text())
```

- lastly `selectedItems()` allows me access to all the values by the user, via a list

---

## QTabWidget

- just like any modern day web browser, tabbing is essential for user navigation
- to set up this structure within my own ui, i can follow these steps:

1. create an instance of `QTabWidget(self)`, which will hold my tabs

```python
    tab_widget = QTabWidget(self)
```

2. create a `QWidget()` object, then create a `QHBoxLayout()` for the contents

```python
    widget_form = QWidget()
    label_name = QLabel("Full name:")
    line_edit_name = QLineEdit()
    form_layout = QHBoxLayout()
```

3. adding various contents now to the layout, then in turn the layout to the widget

```python
    form_layout.addWidget(label_full_name)
    form_layout.addWidget(line_edit_full_name)
    widget_form.setLayout(form_layout)
```

4. i can now do this process over and over for new widgets, later adding them to `QTabWidget`

```python
    tab_widget.addTab(widget_form, "Users Details")
    tab_widget.addTab(widget_next, "New Tab Test")
```

5. lastly i create a layout to hold the whole tabbed widget, then setting said layout to `self`

```python
    layout = QVBoxLayout()
    layout.addWidget(tab_widget)

    self.setLayout(layout)
```

- signals for `QTabWidget` include; `currentChanged`, `tabBarClicked`, `tabCloseRequest`
- virtual functions also include; `initStyleOption`, `tabInserted` and `tabRemoved`

---

## QTComboBox + Important Recap

- allows me to create drop down boxes in my windows
- created again by calling `QComboBox(self)`, with items being added via `self.object.addItem()`
- note; w/e is selected means it is the "current item" in the combo-box

note:

- when i created the object first time, i did not make it a "instance attribute" of my class
- because of this i found that when i wanted to later access it, i was unable to
- this is of course because the object as it was would only exist within `__init__`
- meaning later in the program, its scope would not reach any of my functions
- which is why assigning the widget to the class/object via `self` is so important

- note; "parenting" a widget is different and also relative to this line of code
- `QComboBox(self)` is an example of this
- the objects parent is `self` (ie. current window) meaning;
- it will appear inside the window/parent widget
- when the window/widget is closed the object is consequently destroyed
- but this does not mean im creating a python variable to access outside of `__init__`
- ie. `print(self.box.currentText())` will not be possible

* now i have a drop down box that the user can view/select values, i now need to add functionality
* to do this i will need to utilize `QComboBox` methods;
* `self.box.currentText()` allowing me access to the current selected items text
* `self.box.currentIndex()` again allowing me access to the currently selected index
* and `self.box.count()` will allow me to grab the amount of values within the `QComboBox`

```python
class tab_test(QWidget):
    def __init__(self):
        super().__init__()

        self.box = QComboBox(self)

        self.box.addItem("Graves")
        self.box.addItem("Azir")
        self.box.addItem("Mundo")
        self.box.addItem("Darius")
        self.box.addItem("Luciano")

        button_current_value = QPushButton("Current Value")
        button_current_value.clicked.connect(self.current_value)
        button_set_current = QPushButton("Set value")
        button_set_current.clicked.connect(self.set_value)
        button_get_values = QPushButton("Get values")
        button_get_values.clicked.connect(self.get_values)

        layout = QVBoxLayout()
        layout.addWidget(self.box)
        layout.addWidget(button_current_value)
        layout.addWidget(button_set_current)
        layout.addWidget(button_get_values)
        layout.addSpacing(100)

        self.setLayout(layout)

    def current_value(self):
        print("Current item:", self.box.currentText())
        print("Current index:", self.box.currentIndex())

    def set_value(self):
        index_input = input("What index would you like? ")
        try:
            up_index = int(index_input)
        except ValueError:
            print("Input invalid")
            return

        temp = self.box.count()

        if up_index > 0 or up_index < temp:
            if up_index == 0 or up_index == temp + 1:
                self.box.setCurrentIndex(up_index)
            else:
                self.box.setCurrentIndex(up_index - 1)
        else:
            print("Input invalid")

    def get_values(self):
        for i in range(self.box.count()):
            print(f"index ({i}) : ", self.box.itemText(i))
```

note:

1. `QComboBox(self)` made and stored within the class, meaning its accessible outside of `__init__`
2. values within drop down box are made using `self.box.addItem("")`
3. i can now create functionality, here im creating signals/slots
4. widgets then added to layout + `.addSpacing` then set as `QWidget`'s layout
5. i created my methods using premade functions accessing `QComboBox` values

- ie. `currentText()`, `currentIndex()`, `count()`, `itemText()` and `setCurrentIndex()`
- which is why it was so important to make `QComboBox(self)` accessible
- note; other signals include `activated`, `currentIndexChanged`, `highlighted` and `textHighlighted`
- i should always always be checking the documentation whenever using a widget

---

## Qt Designer & Creator

- is a program that allows me to build user interfaces just by dragging and dropping elements
- the program produces a ".ui" file, we can then import this file into my pyside application
- i must download this program separately to be able to use "Qt Designer" & "Qt Creator"

---

## Qt Designer

- in my first task, im aiming to simply use the program to create a form to collect names/job info
- to later import my work into my own pyside application

note:

- first ive created a folder to save all my user interface files
- clicking "new form" i was able to select from various examples of widget/form templates
- i selected a simple "widget" template so i could add all the functionality i need myself
- to achieve the format i was after, i required two labels, line edits and one submission button

- its important for me to keep in mind my "top level" widgets name, shown in the "objectName" property

- i also edit the "objectName" of all my widgets, so i can reference them later in my python code
- ie. "fullName_lineEdit", "occupation_lineEdit" and "submit_pushButton"

- next i am able to select my widgets and create a layout for them
- this is done by clicking a layout option from the toolbar menu above, here i choose a "vertical layout"
- im also able to click on the "top level widget" and select a layout for all of my widgets
- i can then manually reshape my widget to create a design style i want
- next i can save the widget as "widget.ui"

---

## QUiLoader

- `QUiLoader` is a class accessed through the `PySide6.QtUiTools` module
- it allows me to load my designed widgets into my programs
- using `loader.load("", None)` to load my widget files (on system), into my program
- producing said object in code, ie. `window = loader.load("userdata.ui", None)`

- to be able to access the values within my object, i will have to reference the various "objectName" values
- ie. `print(window.fullName_lineEdit.text())` would allow me access to the "line edits" value in question

- we are also able to create signals to my methods/slots in python
- utilizing the "objectName" again of my submit button, or any signal that widget my offer
- `window.submit_pushButton.clicked.connect(my_method)` will allow me to add functionality
- note; `window` is used as that is the name of the object produced by the `loader.load` call
- `window.show()` will be needed within python, as it will not by default if not prompted

* `QUiLoader` however will come with a performance penalty, because the widget is loaded in "run time"
* so we are effectively trading user experience for ease of development, which should be avoided

* note; before using `loader` i must create this object via calling the class `loader = QUiLoader()`
* also i need to remember that if i want to access text within a widget, `.text()` is needed
* note; when running my tests, i really did notice a big delay when running the application!

---

## QUiLoader via Class

- a better way of to using `QUiLoader` is by wrapping the loaded ui inside a class importing `QObject`

```python
loader = QUiLoader()

class UserInterface(QtCore.QObject):
    def __init__(self):
        super().__init__()
```

- class structure allows signals/slots, logic, and widget access to live together
- and importing `QtCore.QObject` gives me essential qt functionality;
- signal/slot system, connects or defines custom signals
- parent/child memory management, stores variables/functionality and prevents leaks when parent deleted
- "event loop integration", supports the object by allowing the handling of qt events, threads and timers
- effectively allowing me to reconstruct the ".ui" file’s widget tree inside my new class
- `__init__()` loads the ".ui" file once it builds all widgets (`QLineEdit`, `QPushButton`, labels, layouts)
- which avoids repeated loading of the qt designed widget which slowed my program down so much!
- with the ".ui" loaded on object creation only, improving loading times
- plus keeps the widgets state, meaning all user input and any extra values are not lost
- class methods can then be added all within the same part of the code
- separating the ui design in qt designer from my python logic

```python
app = QtWidgets.QApplication(argv)
loader = QUiLoader()

class UserInterface(QtCore.QObject):
    def __init__(self):
        super().__init__()
        self.ui = loader.load("assets\widget.ui", None)
        self.ui.submit_pushButton.clicked.connect(self.print_test)

    def show(self):
        self.ui.show()

    def print_test(self):
        name = self.ui.fullName_lineEdit.text()
        job = self.ui.occupation_lineEdit.text()

        if name == "":
            print("Test button clicked with no input")
        else:
            print(f"Name: {name}")
            print(f"Job:  {job}")


window = UserInterface()
window.show()

app.exec()
```

- note; i forgot to add:

```python
    def show(self):
        self.ui.show()
```

- originally into my class, meaning i could not show the widget without the method being called
- as `window.show()` will only show the container widget and not any loaded ".ui" content

---

## Compiling User Interface Files to Python

- now im learning how i can compile my user interface file into python code
- allowing me to avoid the performance penalty for the user at the cost of my developing time

note:

- the top level widget can be something such as `QMainWindow`, `QWidget` or `QWindow`
- in the original ".ui" file, the top level widget will have a class name within qt designer
- before this, i thought i had to remember the "objectName" but this is not the case
- as its the name of the "top level widget" not its type name...
- by "default" it will be the type/name of the top level widget, but this can be changed manually

- to convert the ".ui" file to python code, i will use `pyside6-uic widget.ui > ui_widget.py`
- via this command pyside6-uic automatically generates a python class name
- using the format; `top level widget Widget → class Ui_Widget`
- the generated python file usually follows the convention `ui_<widgetname>.py`
- ie. `Ui_Widget → ui_widget.py` or `Ui_MainWindow → ui_mainwindow.py`
- note; the `pyside6-uic` compiler was installed alongside `pyside6`

- i will need to remember the top level widget name because the generated class depends on it
- if i rename the widget in qt designer, the generated class and file names will change
- also when importing into my main project, i need to use; `from ui_widget import Ui_Widget`

- so to sum it all up;
- widget.ui <- file generated by qt designer
- ui_widget.py <- the file we get after running pyside6-uic command
- widget.py <- my own python file with a class inheriting from the generated one

- i will be able to next set up my own class such as this;

```python
class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("")
```

note:

- `Ui_Widget` is the auto-generated class from pyside6-uic
- it contains only the ui layout code;
- creating child widgets, setting properties, building layouts
- however `Ui_Widget` is not a qt widget
- meaning it does not provide behavior like events, signals/slots, or interaction

- to make a fully functional widget for my program
- i must also inherit from a qt class (ie. `QWidget`, `QMainWindow`) alongside the imported class

- by calling `setupUi(self)` my widget will be populated with the `qt designed` child widgets
- ie. `QLineEdit`, `QPushButton` and labels will all be included in my example above
- the auto generated child widgets will only exist after `setupUi`
- meaning i will only need to connect their signals or add logic (functionality)
- so i must implement all custom behavior myself
- ie. signal connections, event handlers, and additional methods

- extra note; files may be generated in `UTF-16` which could cause issues for visual studio
- i may need to convert these files to `UTF-8` to avoid any errors

```python
        self.submit_pushButton.clicked.connect(self.print_test)

    def print_test(self):
        print(f"Name: {self.fullName_lineEdit.text()}")
```

- every widget ive created in the ".ui" file has an `objectName` assigned to it
- the `pyside6-uic` compiler uses this name to generate python attributes on the class
- meaning that the qt designer widget names are turn into variables for my class
- ie. `self.fullName_lineEdit`, these variables point to the actual widgets created at runtime

- after calling `setupUi(self)`, all my widgets from the ".ui" file become attributes of the class instance
- ie. `self.fullName_lineEdit`, `self.submit_pushButton` in the examples above

- to access these widgets in code, i can refer to them by these attribute names, which match their `objectNames`
- signals and slots can then be connected normally, ie. `self.submit_pushButton.clicked.connect(self.print_test)`
- methods on the my various widgets like `.text()` or `.setText()` work exactly the same...

---

## Trying it out for myself

- running `pyside6-uic widget.ui > ui_widget.py` while having my `widget.ui` file on hand
- i was given the `ui_widget.py` compiled file, and able to look through its content
- note; checking my new generated file, i can see it is encoding in `UTF-16`
- this will need to be changed to `UTF-8` for visual studio

1. `from ui_widget import Ui_Widget` allows me to import this file, to inherit into my class
2. `class Widget(QWidget, Ui_Widget):` used to create class, with a layout/functionality
3. `self.setupUi(self)` is a method accessed through the imported file

- note; i can see this function within my `ui_widget` file along with "objectName"

```python
app = QApplication(argv)

window = Widget()
window.show()
app.exec()
```

4. after creating the class and adding and signals/slots or other functionality, i can now set up my window;

- calling the `QApplication` class to construct my framework
- creating an object using the class ive just created
- and using said classes inherited functionality to `window.show()` the widget to the user, before running the app
