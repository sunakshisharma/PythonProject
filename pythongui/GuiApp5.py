import tkinter

root=tkinter.Tk()
root.geometry('200x200+100+200')

l1=tkinter.Label(root,text="This is Label 1",bg="red",fg="white")
l2=tkinter.Label(root,text="Label 2",bg="blue",fg="white")
l3=tkinter.Label(root,text="Label 3",bg="green",fg="white")
l4=tkinter.Label(root,text="Label 4",bg="yellow",fg="white")

l1.grid(row=0,column=0)
l2.grid(row=0,column=1)
l3.grid(row=1,column=0,sticky=tkinter.E+tkinter.W)
l4.grid(row=1,column=1)
root.mainloop()
