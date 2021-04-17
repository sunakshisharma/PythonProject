import tkinter

root = tkinter.Tk()
root.geometry('400x200+100+200')

l1 = tkinter.Label(root, text="Number Addition Program",font="Arial 22 bold")
l2 = tkinter.Label(root, text="First No:")
l3 = tkinter.Label(root, text="Second No:")
e1 = tkinter.Entry(root)
e2 = tkinter.Entry(root)
b1 = tkinter.Button(root, text="Add")
b2 = tkinter.Button(root, text="Clear")
b3 = tkinter.Button(root, text="Quit")

l2.grid(row=0, column=0, sticky=tkinter.W)
l2.grid(row=1, column=0, sticky=tkinter.E)
l3.grid(row=2, column=0)
e1.grid(row=1, column=1,sticky=tkinter.E)
e2.grid(row=2, column=1,sticky=tkinter.E)
b1.grid(row=3, column=0,sticky=tkinter.W+tkinter.E)
b2.grid(row=3, column=1,sticky=tkinter.W+tkinter.E)
b3.grid(row=3, column=3,sticky=tkinter.W+tkinter.E)

root.mainloop()
