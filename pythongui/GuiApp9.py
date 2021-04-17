from tkinter import *

root = Tk()
root.geometry('200x200')

def showmsg():
    print("Welcome To Python")

b1 = Button(root, text="Click Me",command=showmsg)

b1.pack()
root.mainloop()
