from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql
class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Login Window")
        self.root.geometry("1550x800+0+0")


        #backgroung image
        self.bg = ImageTk.PhotoImage(file="images/567.jpg")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)




        # login Frame
        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=730, y=200, width=500, height=490)

        Frame_login.Image = ImageTk.PhotoImage(file="images/side1.jpeg")
        Frame_login.Image_Pack = Label(self.root, image=Frame_login.Image).place(x=350, y=200)


        #Title & Subtitle
        title = Label(text="WELCOME    TO   PLACEMENT   MANAGEMENT    SYSTEM",font=("Goudy old style", 35, "bold"), fg="white", bg="#1d4e89").place(x=0, y=30,width=1600)
        title = Label(Frame_login, text="LOGIN HERE", font=("times new roman", 35, "bold"), fg="#6162FF", bg="white").place(x=100,y=20)
        subtitle = Label(Frame_login, text="Students Login Area", font=("Goudy old style", 15, "bold"), fg="#1d1d1d", bg="white").place(x=100, y=80)

        #username
        lbl_user = Label(Frame_login, text="Email", font=("Goudy old style", 15, "bold"), fg="grey", bg="white").place(x=100, y=120)
        self.text_email = Entry(Frame_login, font=("Goudy old style", 15), bg="#E7E6E6")
        self.text_email.place(x=100, y=160, width=320, height=35)

        # password
        lbl_user = Label(Frame_login, text="Password", font=("Goudy old style", 15, "bold"), fg="grey",bg="white").place(x=100, y=210)
        self.text_password = Entry(Frame_login, font=("Goudy old style", 15), bg="#E7E6E6")
        self.text_password.place(x=100, y=250, width=320, height=35)

        #button
        #forget = Button(Frame_login, text="Forgot Password", font=("times new roman", 12, "bold"),cursor="hand2").place(x=100, y=300)
        btn_reg = Button(self.root, text="Register New Account ?",command=self.register_window, font=("times new roman", 19, "bold"),bg="white",cursor="hand2").place(x=440,y=580,width=260,height=40)
        submit = Button(Frame_login,text="Login", command=self.login, font=("Goudy old style", 20), bg="blue",fg="white",cursor="hand2").place(x=160, y=300, width=188, height=40)
        Homescreen = Button(Frame_login, text="Return to Home Screen", command=self.Hs_window, font=("times new roman", 19,"bold"),cursor="hand2").place(x=120, y=390, width=300 , height=40)
#==========Here we connected the Two diffrent Pages===========
    def register_window(self):
        self.root.destroy()
        import register

    def Hs_window(self):
        self.root.destroy()
        import FrontPage

    def login(self):
        if self.text_email.get()=="" or self.text_password.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="student")
                cur=con.cursor()
                cur.execute("select * from register where email=%s and password=%s",(self.text_email.get(),self.text_password.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invailed Username Or Password",parent=self.root)

                else:
                    messagebox.showinfo("Success", "Welcome To Shree L R Tiwari Placement Management", parent=self.root)
                    self.root.destroy()
                    import StuViewOnly
                    con.close()
                    #self.root.destroy()
                    #import register



            except Exception as es:
                messagebox.showerror("Error",f"Error Due to: {str(es)}",parent=self.root)


root = Tk()
obj = Login(root)
root.mainloop()