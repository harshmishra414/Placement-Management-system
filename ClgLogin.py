from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
class Login:
    def __init__(self,root):
        self.root = root
        self.root.title("College Login")
        self.root.geometry("1550x800+0+0")


        #backgroung image
        self.bg = ImageTk.PhotoImage(file="images/567.jpg")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)


        # login Frame
        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=730, y=200, width=520, height=490)

        Frame_login.Image = ImageTk.PhotoImage(file="images/side1.jpeg")
        Frame_login.Image_Pack = Label(self.root, image=Frame_login.Image).place(x=300, y=200)

        #Title & Subtitle
        title = Label(text="WELCOME TO PLACEMENT MANAGEMENT SYSTEM",font=("Goudy old style", 35, "bold"), fg="white", bg="#1d4e89").place(x=0, y=30,width=1550)
        title = Label(Frame_login, text="College Login Here", font=("times new roman", 35, "bold"), fg="#aa5099", bg="white").place(x=70,y=20)
        subtitle = Label(Frame_login, text="Department Login Area", font=("Goudy old style", 15, "bold"), fg="#1d1d1d", bg="white").place(x=100, y=80)

        #username
        lbl_user = Label(Frame_login, text="Username", font=("Goudy old style", 15, "bold"), fg="grey", bg="white").place(x=100, y=120)
        self.username = Entry(Frame_login, font=("Goudy old style", 15), bg="#E7E6E6")
        self.username.place(x=100, y=160, width=320, height=35)

        # password
        lbl_user = Label(Frame_login, text="Password", font=("Goudy old style", 15, "bold"), fg="grey",bg="white").place(x=100, y=210)
        self.password = Entry(Frame_login, font=("Goudy old style", 15), bg="#E7E6E6")
        self.password.place(x=100, y=260, width=320, height=35)

        #button
        #forget = Button(Frame_login, text="Forgot Password", font=("Goudy old style", 12, "bold"), fg="grey",bg="white").place(x=100, y=300)
        submit = Button(Frame_login,command=self.check_function, text="Login ", font=("Goudy old style", 30), bg="#aa5099",fg="white").place(x=200, y=330, width=120, height=40)
        HomeScreen = Button(Frame_login,  text="Return To Home Screen",command=self.HomeScreen_window, font=("Goudy old style", 19),bg="white", fg="black",bd=3).place(x=120, y=400, width=290, height=40)
        #HomeScreen = Button(Frame_login, text="Home Screen", command=self.HomeScreen_window,font=("Goudy old style", 30), bg="#aa5099", fg="white").place(x=250, y=330, width=220,height=40)


    def check_function(self):
        if self.username.get()=="" or self.password.get()=="":
            messagebox.showerror("Error", "All fields are required",parent=self.root)
        elif self.username.get()!="Suraj4542" or self.password.get()!="4542":
            messagebox.showerror("Error", "Invailed username or password",parent=self.root)
        else:
            messagebox.showinfo("Welcome To Placement Management System", f"welcome{self.username.get()}")
            self.root.destroy()
            import StuDetails

    def HomeScreen_window(self):
        self.root.destroy()
        import FrontPage

    '''def Clg_window(self):
        self.root.destroy()
        import StuDetails'''


root = Tk()
obj = Login(root)
root.mainloop()