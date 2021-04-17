import tkinter
import tkinter.font as tkFont

root=tkinter.Tk()
root.geometry("600x200")
# myLable1=tkinter.Label(root,text="Welcome to Python project batch")
# myLable2=tkinter.Label(root,text="Python Rocks!")

# myLable1 = tkinter.Label(root, text="Welcome to Python project batch", fg="blue", bg="red")
myLable1 = tkinter.Label(root, text="Welcome to Python project batch")

# myLable1.config(bg="limegreen",fg="red")
# myLable1 = tkinter.Label(root, text="Welcome to Python project batch",font="Arial 22 bold")
# myLable1 = tkinter.Label(root, text="Welcome to Python project batch",font=myfont)
# myLable1.config(font="verdana 28 italic")
# myLable1.config(font=("Times new roman", 20 ,"italic"))

# myfont=tkFont.Font(weight="bold",family="helvetica")
# myLable1 = tkinter.Label(root, text="Welcome to Python project batch",bg="yellow",width=30,borderwidth=2,relief="raised")
# myLable1.pack()

# root.config(bg="yellow")

# myLable2.pack()
myfont=tkFont.Font(size=22)
myLable1 = tkinter.Label(root, text="Hello\nIndia",font=myfont,borderwidth=2,relief="solid",width=20,height=4,anchor="e")
myLable1.pack()
root.mainloop()
