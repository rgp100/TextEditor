from tkinter import *
import os
from subprocess import Popen

def shitpad():
		outer = Tk()
		outer.title('ShiText')
		outer.mainloop()

devnull = open(os.devnull, 'wb') # use this in python < 3.3
# python >= 3.3 has subprocess.DEVNULL
Popen(['python3', 'multipleinstances.py'], stdout=devnull, stderr=devnull)
