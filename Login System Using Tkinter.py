from tkinter import* 
from tkinter import messagebox

root=Tk()
root.title("Login")
root.geometry("925x500+300+200")
root.configure(bg="")
root.resizable(False,False)

img = PhotoImage(file="images/login.png")
Label(root, image=img, bg="white").place(x=50, y=50)

frame = Frame(root, width=350, height=350, bg="red")
frame.place(x=480, y=70)

heading = Label(frame, text="Sign in", fg="#57a1f8", bg="white", font=("Microsoft Yahei Light", 23, "bold"))


root.mainloop()