#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import Tk, BOTH
from tkinter.ttk import Frame

class Example(Frame):
  
    def __init__(self):
        super().__init__()  
        
        self.initUI()
        
        
    def initUI(self):     
         
        self.master.title("Centered window")
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()
        

    def centerWindow(self):
      
        w = 290
        h = 150
        #size of window
        sw = self.master.winfo_screenwidth()
        sh = self.master.winfo_screenheight()
        #determine sizes of screen
        x = (sw - w)/2
        y = (sh - h)/2
        #necessary x and y coord
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))


def main():
  
    root = Tk()
    ex = Example()
    root.mainloop()  


if __name__ == '__main__':
    main()   