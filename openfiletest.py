import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

print(file_path)
f = open(file_path)
f = f.read()
print(f)

# need to create a new window and insert the text into it