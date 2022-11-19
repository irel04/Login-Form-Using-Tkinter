from tkinter import* 
from tkinter import messagebox

root=TK()
root.title("Login")
root.geometry("925x500+300+200")
root.configure(bg="")
root.resizable(False,False)

img = PhotoImage(file="images/login.png")
Label(root, image=img, bg="white").place(x=50, y=50)