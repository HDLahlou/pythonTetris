from tkinter import Tk, Label, Button, StringVar

class myGui:
	LABEL_TEXT = [
	"Text 1",
	"Text 2",
	"Text 3"
	]
	def __init__(self, master):
		self.master = master
		master.title('Simple GUI')

		self.label_index= 0
		self.label_text = StringVar()
		self.label_text.set(self.LABEL_TEXT[self.label_index])
		self.label = Label(master, textvariable=self.label_text)
		#bind takes an additional paramter an event object
		self.label.bind("<Button-1>", self.cycle_label_text)
		self.label.pack()

		self.greet_button = Button(master, text="Greet", command= self.greet)
		self.greet_button.pack()

		self.close_button = Button(master, text="Close", command = master.quit)
		self.close_button.pack()

	def greet(self):
		print("Greetings!")

	def cycle_label_text(self, event):
		self.label_index +=1
		self.label_index %=len(self.LABEL_TEXT) #wraps around
		self.label_text.set(self.LABEL_TEXT[self.label_index])


root = Tk()
my_gui = myGui(root)
root.mainloop()