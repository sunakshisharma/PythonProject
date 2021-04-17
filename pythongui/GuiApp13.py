from tkinter import *

count = 0
root = Tk()
root.geometry('300x200')
obj = IntVar()


def showcounter():
    obj.set(obj.get() + 1)


b1 = Button(root, text="Click Me", command=showcounter)
l1 = Label(root, textvariable=obj)
b1.pack()
l1.pack()
root.mainloop()
