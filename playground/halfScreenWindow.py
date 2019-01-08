from tkinter import Tk, BOTH
from tkinter.ttk import Frame

class guiWindow(Frame):

	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):

		self.master.title("1/2 of Screen")
		self.pack(fill=BOTH, expand=1)
		self.windowSize()


	def windowSize(self):

		sw = self.master.winfo_screenwidth()
		sh = self.master.winfo_screenheight()

		w = sw*.707107
		h = sh*.707107

		x = (sw - w)/2
		y = (sh - h)/2

		self.master.geometry('%dx%d+%d+%d' % (w,h,x,y))

def main():

	root = Tk()
	app = guiWindow()
	root.mainloop()

if __name__ == '__main__':
	main()