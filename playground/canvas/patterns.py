from tkinter import *

master = Tk()

w = Canvas(master, width=200, height = 100)
w.pack()

w.create_line(0,0,200,100)
w.create_line(0,100,200,0, fill="red", dash=(4,4))

w.create_rectangle(50,25,150,75, fill="blue")

i = w.create_line(xy, fill="red")

w.coords(i, new_xy)
w.itemconfig(i, fill="blue")

w.delete(i)

w.delete(All)

mainloop()