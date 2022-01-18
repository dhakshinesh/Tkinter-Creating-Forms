#importing the tkinter module
import tkinter
from tkinter import *

#Assigning a wimdow
root = tkinter.Tk()

#text field : username
Label(root, text="Username").grid(row = 0,column = 0)
Entry(root).grid(row = 0,column = 1)
#text field : password
Label(root, text="Password").grid(row = 1,column = 0)
Entry(root).grid(row = 1,column = 1)
#Checkbox field
Checkbutton(root,text="Remember?").grid(row=2, column=1)
#Submit button
Button(root, text = 'Submit').grid(row=3, column=0)
root.mainloop()