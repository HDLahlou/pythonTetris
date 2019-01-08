#create a line from (10,10) to (200,50)
#canvas.create_line(10,10,200,50)
#method will return an item id (int) that can be used to uniquely refer to this item, every item will get its own id
#to create a canvas for drawing, will create a canvas widget, attach event bindings to it to capture mouse clicks and drags
#when first click the mouse, we will remember that location as start
#then create a line item going from the start position to the mouses current mouse position
#the current position then updates to become the new starting position

#Changing attributes of item when creating (color red width 3 pix)
#canvas.create_line(10,10,200,50, fill='red', width=3)

#configuring and updating items
#id = canvas.create_line(0,0,10,10, fill='red')
#...
#canvas.itemconfigure(id, fill='blue', width=2)

#Binding to an object /tags
#canvas.tag_bind(id, '<1>', ...)
#item specific tab_bind and widgetlevel bind

#Tags, every canvas item has a unique id number
#Many items can have the same tag, doesnt have to be unique
#Can use a tag in the same scenario that you can use an item id
#Tags good 

"""
>>> c = Canvas(root)
>>> c.create_line(10, 10, 20, 20, tags=('firstline', 'drawing'))
1
>>> c.create_rectangle(30, 30, 40, 40, tags=('drawing'))
2
>>> c.addtag('rectangle', 'withtag', 2)

Withtag will tkae an individual item or a tag and apply to all items that have that tag

>>> c.addtag('polygon', 'withtag', 'rectangle')
>>> c.gettags(2)
('drawing', 'rectangle', 'polygon')
>>> c.dtag(2, 'polygon')
>>> c.gettags(2)
('drawing', 'rectangle')	
>>> c.find_withtag('drawing')
(1, 2)
"""
#To delete items use the delete method. To change size and position use coords method
#calling coords without new coords returns current location
#to move an item from a particular position to another use the move method
#Items are ordered in a stacking order, if an item later in the stack overlaps the coordinate of an item below it
#the item ontop will be drawn on top of the lower item, raise and lower adjust stack order

#SCROLLING
#Can attach scrollbars via xview and yview
#Scrollregion tells Tk how large the canvas surface is
#bind doesnt acocunt for scrolling, will treat the new left corner as 0,0
#canvasx and canvasy will translate the position on screen
from tkinter import *
from tkinter import ttk

lastx, lasty = 0, 0
color = "black"

def setColor(newcolor):
    global color
    color = newcolor
    canvas.dtag('all', 'paletteSelected')
    canvas.itemconfigure('palette', outline='white')
    canvas.addtag('paletteSelected', 'withtag', 'palette%s' %color)
    print('palette%s' %color)
    canvas.itemconfigure('paletteSelected', outline='#999999')


def xy(event):
	global lastx, lasty
	lastx, lasty = event.x, event.y

def addLine(event):
    global lastx, lasty
    canvas.create_line((lastx, lasty, event.x, event.y), width=5, fill=color, tags='currentline')
    lastx, lasty = event.x, event.y


def doneStroke(event):
	canvas.itemconfigure('currentline', width=1)

root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0,weight=1)

canvas = Canvas(root)
canvas.grid(column=0, row=0, sticky= (N,W,E,S))
canvas.bind("<Button-1>", xy)
canvas.bind("<B1-Motion>", addLine)
canvas.bind("<B1-ButtonRelease>", doneStroke)

id = canvas.create_rectangle((10, 10, 30, 30), fill="red", tags=('palette', 'palettered'))
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("red"))
id = canvas.create_rectangle((10, 35, 30, 55), fill="blue", tags=('palette', 'paletteblue'))
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("blue"))
id = canvas.create_rectangle((10, 60, 30, 80), fill="black", tags=('palette', 'paletteblack', 'paletteSelected'))
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("black"))

setColor('black')
canvas.itemconfigure('palette', width=5)

root.mainloop()