from tkinter import *
from tkinter.ttk import Frame
from array import *
from random import *
import time

global grid
global width
global gridWidth
global gridHeight
global c
global w
global shapes
global rotation
global activeBlocks
global totalPoints

# grid is row by column or [y][x]
class GridBlock(object):
    empty = True
    weight = 0
    color = '#999999'
    id = 0

    def __init__(self, empty):
        self.empty = empty

    def make_gridblock(self,empty):
        gridblock = GridBlock(empty)
        return gridblock

    def populate_grid(self,col,row):
        gridArray = []
        for i in range(0,row):
            gridArray.append([])
            for j in range(0,col):
                gridArray[i].append(self.make_gridblock(self, True))

        return gridArray

    def checkRowFull(self, row):
        global grid
        r = len(grid[row])
        for i in range(0,r):
            if grid[row][i].empty:
                return False
        return True

    def redrawGrid(self, newRows, row, col):
        global grid
        global c
        for y in range(0, row):
            if y < newRows:
                c.itemconfigure('%d' %y, fill= '#999999')
            else:
                for x in range(0, col):
                    currentBlock = grid[y][x]
                    c.itemconfigure('%d,%d' %(x,y), fill = currentBlock.color)



    def settleGrid(self):
        global totalPoints
        global activeBlocks
        global grid
        global c
        row = len(grid)
        col = len(grid[0])
        points = 0
        for b in activeBlocks:
            grid[b.y][b.x].empty = False
            grid[b.y][b.x].weight = b.weight
            grid[b.y][b.x].color = b.color
            c.itemconfigure('%d,%d' %(b.x, b.y), fill= b.color )
        for y in range(0,row):
            index = row-1-y
            if self.checkRowFull(self,index):
                grid.pop(index)
                points = points+1

        replacementArrays = self.populate_grid(self, c, points)
        grid = replacementArrays + grid
        self.redrawGrid(self, points, row, col)
        totalPoints = totalPoints + points


class Coordinate(object):
    x = 0
    y = 0

    def __init__(self, x,y):
        self.x = x
        self.y = y

    def make_coordinate(x,y):
        co = Coordinate(x,y)
        return co

    def coordinateArray(self, *arg):
        index = 1
        x = None
        y = None
        array = []

        for a in arg:
            if index%2 == 1:
                x = a
            if index%2 == 0:
                y = a
            if x!= None and y != None:
             #   print('array')
                array.append(Coordinate.make_coordinate(x,y))
                x = None
                y = None
            index +=1
       # print (array)
        return  array

class Block(object):
    x = 0
    y = 0
    color = ""
    weight = 0

    # The class "constructor" - It's actually an initializer

    def __init__(self, x,y,color,weight):
        self.x = x
        self.y = y
        self.color = color
        self.weight = weight

    def make_block(x,y,weight):
        colors = [ "white", "yellow", "blue","red"]
        block = Block(x,y,colors[weight-1],weight)
        return block

    """
    Bottom Right Square =  Anchor
    ----4-----
    L = (-1,0) (0,-2) (0,-1) (0,0)

    n = (-3,0) (-2,-1) (-1,-1) (0,0)

    I = (0,-3) (0,-2) (0,-1) (0,0)

    T = (-1,-1) (0,-1) (1,1) (0,0)

    S = (-1,0) (0,-1) (1,-1) (0,0)

    O = (-1,-1) (0,-1) (-1,0) (0,0)
    ----3-----
    3 = (-2,0) (-1,0) (0,0)

    e = (-1,0) (0,-1) (0,0)

    v = (-2,0) (-1,-1) (0,0)
    ----2-----
    2 = (-1,0) (0,0)

    z = (-1,-1)(0,0)
    ----1-----
    1 = (0,0)

    To Rotate, apply pi/2
    (x,y)
    (y,-x)
    (-x,-y)
    (-x,y)

    Matrix
    [  0   1 ]
    [ -1   0 ]
    """
    def populateShapesDict(self):
        global shapes
        shapes = {'L': None, 'T': None, 'I': None, 'O': None, 'n': None, 'S': None, "3": None, 'e': None, 'v': None, '2': None, 'z': None, '1': None}
        print('Coord')
        print(Coordinate.coordinateArray(Coordinate, -1, 0, -2, 0, 0, -1, 0, 0))
        shapes['L'] = Coordinate.coordinateArray(Coordinate, -1, 0, 0, -2, 0, -1, 0, 0)
        shapes['T'] = Coordinate.coordinateArray(Coordinate, -1, -1, 0, -1, 1, 1, 0, 0)
        shapes['I'] = Coordinate.coordinateArray(Coordinate, 0, -3, 0, -2, 0, -1, 0, 0)
        shapes['O'] = Coordinate.coordinateArray(Coordinate, -1, -1, 0, -1, -1, 0, 0, 0)
        shapes['n'] = Coordinate.coordinateArray(Coordinate, -3, 0, -2, -1, -1, -1, 0, 0)
        shapes['S'] = Coordinate.coordinateArray(Coordinate, -1, 0, 0, -1, 1, -1, 0, 0)
        shapes['3'] = Coordinate.coordinateArray(Coordinate, -2, 0, -1, 0, 0, 0)
        shapes['e'] = Coordinate.coordinateArray(Coordinate, -1, 0, 0, -1, 0, 0)
        shapes['v'] = Coordinate.coordinateArray(Coordinate,-2, 0, -1, -1, 0, 0)
        shapes['2'] = Coordinate.coordinateArray(Coordinate, -1, 0, 0, 0)
        shapes['z'] = Coordinate.coordinateArray(Coordinate, -1, -1, 0, 0)
        shapes['1'] = Coordinate.coordinateArray(Coordinate, 0, 0)
        return shapes

    def randomizeBlock(self, shapes):
        keys = shapes.keys()
        keyValue = sample(keys,1)
        weightValue = randint(0,3)
        self.make_shapes(self,shapes, keyValue, weightValue)

    def canSpawn(self):
        global activeBlocks
        global grid
        empty = True
        for b in activeBlocks:
            if b.y > -1:
                empty = grid[b.y][b.x].empty

        return empty

    #initializes shape of block
    def make_shapes(self,shapes, key, weight):
        global width
        global activeBlocks
        print(shapes)
        print('Make Shapes')
        activeBlocks = []
        print(key)
        shape = shapes.get(key[0])
        print(shape)
        index = len(shape)
        print(index)
        for i in range (0, index):
            x = (shape[index - (i+1)].x) +4
            y = (shape[index - (i+1)].y)
            activeBlocks.append(Block.make_block(x,y,weight))
        if self.canSpawn(self):
            self.draw_shapes(self)

    #main method for displaying blocks
    def draw_shapes(self):
        global activeBlocks
        global grid
        global width
        global c
        print('Drawing Shapes')
        #checks to see if the blocks are in the grid yet
        c.itemconfigure('activeBlock', fill = '#999999')
        c.dtag('all','activeBlock')
        for i in range(0, len(activeBlocks)):
            x = activeBlocks[i].x
            y = activeBlocks[i].y
            print('x:%d Y:%d' %(x,y))
            if y > -1:
                c.addtag('activeBlock', 'withtag', '%d,%d' %(x, y))
               # print('Coloring: %s' %activeBlocks[i].color )
                #print(c.find_withtag('%d,%d' %(x, y)))
                c.itemconfigure('activeBlock', fill=activeBlocks[i].color)
        print(c.find_withtag('activeBlock'))





#Logic check statements
    #supplementary functions
    def inRange(self,x,y):
        global grid
        global gridWidth
        global gridHeight
        global width

        if x <= 0 or x >= gridWidth/width or y >= gridHeight/width:
            print('Outside of range')
            return False
        else:
            return True

    def isEmpty(self,col,row):
        if self.inRange(self,col,row):
            return grid[row][col].empty


    def checkDown(self, x, y):
        if self.inRange(self,x,y) and self.inRange(self, x,y+1):
            if (self.isEmpty(self, x,(y+1)) == True):
                return True
        return False
        #mod: -1 means left 1 means right
    def checkHorizontal(self, x,y, mod):
        if self.inRange(self,x,y) and self.inRange(x+mod, y):
            if self.isEmpty(x+mod, y) == True:
                return True

        return False

    def moveDown(self):
        global activeBlocks
        for b in activeBlocks:
            b.y = b.y+1

    def moveHorizontal(self, mod):
        global activeBlocks
        for b in activeBlocks:
            b.x = b.x+mod


#Natural movement of block
    def moveBlockDown(self):
        global activeBlocks
        active = True
        for  b in activeBlocks:
            active = self.checkDown(self,b.x, b.y)
            if active == False:
                break
        if active:
            print('%s' %(active))
            self.moveDown(self)
            self.draw_shapes(self)
        else:
            print('Grid settled')
            GridBlock.settleGrid(GridBlock)
        return active

    def moveBlockHorizontal(self, mod):
        global activeBlocks
        move = True
        for b in activeBlocks:
            move = self.checkHorizontal(self,b.x,b.y, mod)
        if move:
            self.moveHorizontal(self,mod)
            self.draw_shapes(self)


def centerWindow(self):

    w = 700
    #size of window
    sw = self.master.winfo_screenwidth()
    sh = self.master.winfo_screenheight()
    h = sh
    #determine sizes of screen
    x = (sw - w)/2
    y = (sh - h)/2
    #necessary x and y coord
    self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))

def gridInitSquares(canvas, gridHeight, gridWidth, width):
    global grid
    print("Init squares")
    col = int(gridWidth/width)
    row = int(gridHeight/width)
    for i in range(0, row):
        for j in range(0,col):
            tagString = '%d,%d' %(j,i)
            xTag = 'x=%d' %j
            yTag = 'y=%d' %i
            #print(tagString)
            grid[i][j].id = canvas.create_rectangle((j*width,i*width ,(j+1)*width, (i+1)*width), fill="#999999", tags=(tagString,yTag,xTag))
            #print('id:%s' %grid[i][j].id)



def create_grid(c):
    w= c.winfo_width()
    h= c.winfo_height()
    c.delete('grid_line')
    for i in range(0, w, width):
        c.create_line([(i,0), (i,h)], tag= 'grid_line')
    for i in range(0,h, width):
        c.create_line([(0,i), (w, i)], tag='grid_line')


def startGame(canvas):
    #initiate game, start game loop, delete starting button
    global totalPoints
    global shapes
    global grid
    global c
    #Init Shapes List
    shapes = Block.populateShapesDict(Block)
    startTime = time.time()
    totalPoints = 0
    canvas.itemconfigure('Start', text ="")

    #Main Game Loop
    while totalPoints < 15:
        active = True
        Block.randomizeBlock(Block, shapes)
        while active:
            if (time.time()- startTime > 1):
                print(startTime)
                startTime = time.time()
                active = Block.moveBlockDown(Block)



def main():
    #defining global variables
    global gridWidth
    global gridHeight
    global width
    global grid
    global c
    #Global Def
    width = 50
    gridHeight = 750
    gridWidth = 500
    x = int(gridWidth/width)
    y = int(gridHeight/width)
    grid = GridBlock.populate_grid(GridBlock, x, y)
    #Canvas Definitions
    root = Tk()
    w = Canvas(root, height=950, width = 700, bg='black')
    w.master.title("Grid")
    w.pack(fill=BOTH, expand=1)
    centerWindow(w)
    c = Canvas(w, height = gridHeight, width = gridWidth, bg='white')
    c.pack(side=BOTTOM)
    gridInitSquares(c, gridHeight, gridWidth, width)
    c.bind('<Configure>', lambda x: create_grid(c))
    #Canvas Init
    startLabel = c.create_text((gridWidth/2),(gridHeight/2), font= 20, text = "Start", tags ='Start')

    #Canvas Binding
    c.tag_bind(startLabel, "<Button-1>", lambda x: startGame(c))
    c.bind('a', lambda x: Block.moveBlockHorizontal(Block,-1))
    c.bind('d', lambda x: Block.moveBlockHorizontal(Block,1))

    root.mainloop()




if __name__ == '__main__':
    main()   