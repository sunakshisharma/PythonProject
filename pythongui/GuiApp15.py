from tkinter import *

root = Tk()
root.geometry('300x200')

l1 = Label(root, height=3, width=20, bg="white")
b1 = Button(root, text="Red", width=6, command=lambda: l1.config(bg="red"))
b2 = Button(root, text="Green", width=6, command=lambda: l1.config(bg="green"))
b3 = Button(root, text="Blue", width=6, command=lambda: l1.config(bg="blue"))
l1.grid(row=0, column=1)
b1.grid(row=1, column=0)
b2.grid(row=1, column=1)
b3.grid(row=1, column=2)

root.mainloop()
