#imports
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

#main class
class Window(QMainWindow):
    #constructor method
    def __init__(self):
        #inherits mehtod from superclass
        super().__init__()
        self.UiComponents()
        # g_fonts = self.fonts.families()

    def UiComponents(self):
        #Window name
        self.setWindowTitle("Font Display")
        self.width = 1920
        self.height = 1080
        self.setGeometry(100, 100, self.width, self.height)
        self.fonts = QFontDatabase()

        #Set starting x and y position
        self.x = 20
        self.y = 0

        #Set font size
        self.fontSize = 13

        for font in self.fonts.families():
            #moves list when it runs out of space
            if self.y > 950:
                self.y = 0
                self.x += 230
            show_font = QLabel(str(font), self)
            show_font.setAlignment(Qt.AlignCenter)
            show_font.setGeometry(self.x, self.y, 300, 100)

            show_font.setFont(QFont(str(font), self.fontSize))
            #Moves next font down
            self.y += 20

        self.show()








if __name__ == '__main__':

#Creates app object, initialize Qt app
    App = QApplication(sys.argv)

#Creates window class
    window = Window()

#Starts app, everything is blocked until app is exited
    sys.exit(App.exec())