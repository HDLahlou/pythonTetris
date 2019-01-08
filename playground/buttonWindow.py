#!/usr/bin/python3
# -*- coding: utf-8 -*-

from tkinter import Tk, BOTH
#Tkinter supports theming of widgets
from tkinter.ttk import Frame, Button, Style

class Example(Frame):
  
    def __init__(self):
        super().__init__()   
         
        self.initUI()
        
        
    def initUI(self):
        #Apply a theme for our widgets (clam, default, alt, classic)
        self.style = Style()
        self.style.theme_use("default")
        
        self.master.title("Quit button")
        self.pack(fill=BOTH, expand=1)
        #Create instance of button widget, parent is frame container
        #Provide label and command
        quitButton = Button(self, text="Quit",
            command=self.quit)
        #place geometry to position absolute coordinates
        quitButton.place(x=50, y=50)


def main():
  
    root = Tk()
    root.geometry("250x150+300+300")
    app = Example()
    root.mainloop()  


if __name__ == '__main__':
    main()   