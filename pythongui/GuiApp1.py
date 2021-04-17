import tkinter
root=tkinter.Tk()
root.title("My GUI")
# img=tkinter.PhotoImage(file="path of the image")
# root.iconphoto(root,img)  this 2 line sis for change the image of the root window only support png nd gif extention image
# root.geometry("400x400+200+300")
w=root.winfo_screenmmwidth()
h=root.winfo_screenheight()
width=w//2
height=h//2
x=w//4
y=w//4
# root.geometry(str(width)+"x"+str(height)+"+"+str(x)+"+"+str(y))
root.geometry(f"{width}x{height}+{x}+{y}")
root.resizable(True,False)
root.mainloop() 