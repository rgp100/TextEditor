from tkinter import *
from tkinter import filedialog
import os
from subprocess import Popen
from subprocess import DEVNULL

class Notepad:

	def __init__(self, master=None):
		"""variables are initiated here """

		self.file_path = None #this will be changed when a file is opened, or saved
		self.master = master
		self.frm1 = Frame(master)

		scrollbar = Scrollbar(master)
		scrollbar.pack(side=RIGHT, fill=Y)

		self.textBox = Text(master, wrap=WORD, yscrollcommand=scrollbar.set)
		self.textBox.pack()

		scrollbar.config(command=self.textBox.yview)

		self.frm1.pack()
		self.menuBar()

	def newPad(self):
		devnull = DEVNULL
		Popen(['nohup', 'python3', '/home/boo/Desktop/Python/shitext/shiText.py'], stdout=devnull, stderr=devnull)

	def saveFile(self):
		if (self.file_path == None):
			self.saveFileAs()
		else:
			outfile = open(self.file_path, "w")
			# Write to the file
			outfile.write(self.textBox.get(1.0, END)) 
			outfile.close() # Close the output file	
				
	def saveFileAs(self):
		self.file_path = filedialog.asksaveasfilename()
		outfile = open(self.file_path, "w")
		# Write to the file
		outfile.write(self.textBox.get(1.0, END)) 
		outfile.close() # Close the output file

	def menuBar(self):
		"""This builds the menu bar"""

		menu = Menu(self.master)
		self.master.config(menu=menu)

		#File Menu
		fyle = Menu(menu)
		fyle.add_command(label='New',command=self.newPad)
		fyle.add_command(label='Open File',command=self.open_file)
		fyle.add_command(label='Save', command=self.saveFile)
		fyle.add_command(label='Save As',command=self.saveFileAs)
		fyle.add_command(label='Exit', command=outer.destroy)
		menu.add_cascade(label='File',menu=fyle)

		#Edit Menu
		edit = Menu(menu)
		edit.add_command(label='Cut')
		edit.add_command(label='Copy')
		edit.add_command(label='Paste')
		edit.add_command(label='Undo')
		edit.add_command(label='Redo')
		menu.add_cascade(label='Edit',menu=edit)

		#View Menu
		view = Menu(menu)
		view.add_command(label='Line Numbers')
		menu.add_cascade(label='View', menu=view)


		#Help Menu
		help = Menu(menu)
		help.add_command(label='About')
		menu.add_cascade(label='Help',menu=help)	

	def open_file(self): # need to fix this to open in a new window
		"""This will open a file and insert the contents into the text widget"""
		self.file_path = filedialog.askopenfilename()
		f = open(self.file_path)
		freader = f.read()
		self.textBox.insert(END, freader)


outer = Tk()
outer.title('ShiText')
inner = Notepad(outer)
outer.mainloop()

