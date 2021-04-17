from tkinter import *

root = Tk()
root.geometry('200x200')


def showmsg():
    l1.config(text="Welcome To Python")
    l1.pack()


b1 = Button(root, text="Click Me", command=showmsg)
l1 = Label(root)
b1.pack()

root.mainloop()
