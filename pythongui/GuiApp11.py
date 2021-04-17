from tkinter import *
from datetime import *

root = Tk()
root.geometry('300x200')


def showmsg():
    date=datetime.now()
    str=date.strftime("%d-%B-%Y,%H:%M:%S %p")
    l1.config(text=str)


b1 = Button(root, text="Click Me", command=showmsg)
l1 = Label(root,text="Click the button for date and time")
b1.pack()
l1.pack()
root.mainloop()
