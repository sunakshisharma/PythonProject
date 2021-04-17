import tkinter

root=tkinter.Tk()
lbl=tkinter.Label(root,text="Welcome",font="Arial 22 bold",bg="blue",fg="white")
lbl.pack()
print(lbl.keys())
print(lbl['font'])
print(lbl['bg'])

lbl['text']='Good Morning'
lbl['bg']='red'

root.mainloop()
