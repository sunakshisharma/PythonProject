from tkinter import *

count = 0
root = Tk()
root.geometry('300x200')


def showcounter():
    global count
    count = count + 1
    l1.config(text=count)


b1 = Button(root, text="Click Me", command=showcounter)
l1 = Label(root, text="0")
b1.pack()
l1.pack()
root.mainloop()
