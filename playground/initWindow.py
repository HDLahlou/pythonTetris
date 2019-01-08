#!/usr/bin/python3
# -*- coding: utf-8 -*-

#imports TK=k and Frame class, and the constant BOTH
#Tk is used to create a root window
#Frame is container for other widgets
from tkinter import Tk, BOTH
from tkinter.ttk import Frame

#Example class inherits Frame container widget
#calls constructor of our inherited class in the _init_()
class Example(Frame):
  
    def __init__(self):
        super().__init__()
        #delegates creation of the user interface to the initUI()
        self.initUI()
        
    
    def initUI(self):
        #Set title of window, master attribute gives access to the root window Tk
        self.master.title("Simple")
        #pack() method one of 3 geometry managers in Tkinter
        #organizes widgets into horizontal and vertical boxes, here goes the frame widget
        #Frame accessed through self attribute in Tk root window
        #expands in both directions, taking whole client space of the root window
        self.pack(fill=BOTH, expand=1)
        

def main():
    #root window created, main app window, must be created before any widgets
    root = Tk()
    #sets size and positions it on the screen 1) width 2) height 3) X 4) Y coord
    root.geometry("250x150+300+300")
    #Creates instance of application class
    app = Example()
    #main loop, event handling starts from this point, receives events from the window system
    #dispatches them to application widgets
    root.mainloop()  


if __name__ == '__main__':
    main()   