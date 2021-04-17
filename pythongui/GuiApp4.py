import tkinter

root=tkinter.Tk()
root.geometry("600x400")
# img=tkinter.PhotoImage(file="/Users/apple/Desktop/googleIcon.png")
# lbl=tkinter.Label(root,text="Welcome",image=img,compound=tkinter.LEFT)
# lbl.pack()

strobj=tkinter.StringVar()
lbl=tkinter.Label(root,borderwidth=2,relief="solid",textvariable=strobj)
# lbl.pack(fill=tkinter.X,padx=10)
# lbl.pack(fill=tkinter.X,padx=(10,0))
# lbl.pack(fill=tkinter.X,pady=10)
# lbl.pack(fill=tkinter.X,ipadx=10,side=tkinter.LEFT)
lbl.place(x=50,y=40)
strobj.set("Good Evening")


root.mainloop()
