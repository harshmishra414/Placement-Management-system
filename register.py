from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import pymysql
class register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Window")
        self.root.geometry("1550x800+0+0")
        #======Bg Images====
        self.bg=ImageTk.PhotoImage(file="images/567.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        # =======FG======
        self.left = ImageTk.PhotoImage(file="images/side1.jpeg")
        left = Label(self.root, image=self.left).place(x=280, y=170, width=400, height=500)

        #======Register FRAME=====
        frame1=Frame(self.root,bg="white")
        frame1.place(x=680,y=170,width=700,height=500)

        title = Label(text="Shree L R Tiwari College Of Engineering", font=("Goudy old style", 30, "bold"), fg="white",bg="#1d4e89").place(x=0, y=30, width=1550)

        title=Label(frame1,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="white",fg="blue").place(x=150,y=30)
        #============Row1
        #self.var_fname=StringVar()
        f_name = Label(frame1, text="First Name", font=("times new roman", 20, "bold"), bg="white", fg="gray").place(x=50, y=100)
        self.text_fname = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.text_fname.place(x=50, y=130, width=250)
        l_name = Label(frame1, text="Last Name", font=("times new roman", 20, "bold"), bg="white", fg="gray").place(x=370, y=100)
        self.text_lname = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.text_lname.place(x=370, y=130, width=250)

        # =======contact & email=====
        contact = Label(frame1, text="Contact No.", font=("times new roman", 20, "bold"), bg="white", fg="gray").place(x=50, y=170)
        self.text_contact = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.text_contact.place(x=50, y=200, width=250)
        email = Label(frame1, text="E-mail", font=("times new roman", 20, "bold"), bg="white", fg="gray").place(x=370,y=170)
        self.text_email = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.text_email.place(x=370, y=200, width=250)
        # =======Security Questions=====
        question = Label(frame1, text="Security Question", font=("times new roman", 20, "bold"), bg="white",fg="gray").place(x=50, y=240)
        self.cmb_question = ttk.Combobox(frame1, font=("times new roman", 13),state='readonly',justify=CENTER)
        self.cmb_question['values'] = ("Select", "Your First Pet Name", "Your Birth Place", "Your Best Friend Nmae")
        self.cmb_question.place(x=50, y=270, width=250)
        self.cmb_question.current(0)
        answer = Label(frame1, text="Answer", font=("times new roman", 20, "bold"), bg="white", fg="gray").place(x=370,y=240)
        self.text_answer = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.text_answer.place(x=370, y=270, width=250)
        # =======contact & email=====
        password = Label(frame1, text="Password", font=("times new roman", 20, "bold"), bg="white", fg="gray").place(x=50, y=310)
        self.text_password = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.text_password.place(x=50, y=340, width=250)
        cpassword = Label(frame1, text="Confirm-Password", font=("times new roman", 20, "bold"), bg="white",fg="gray").place(x=370, y=310)
        self.text_cpassword = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.text_cpassword.place(x=370, y=340, width=250)
        # ========Terms & Condition=====
        self.var_chk=IntVar()
        chk = Checkbutton(frame1, text="I Agree The Terms and Conditions",variable=self.var_chk, onvalue=1, offvalue=0,font=("times new roman", 15, "bold")).place(x=50, y=380)
        self.btn_img = ImageTk.PhotoImage(file="images/download.jfif")
        btn_register= Button(frame1, image=self.btn_img,bd=0,cursor="hand2",comman=self.register_data).place(x=130, y=420)

        btn_login = Button(self.root, text="Sign in",command=self.studentlogin_window, font=("times new roman", 20), bd=0, cursor="hand2").place(x=400,y=460,width=180)

    def studentlogin_window(self):
        self.root.destroy()
        import studentlogin

    def clear(self):
        self.text_fname.delete(0,END)
        self.text_lname.delete(0, END)
        self.text_contact.delete(0, END)
        self.text_email.delete(0, END)
        self.text_password.delete(0, END)
        self.text_cpassword.delete(0, END)
        self.cmb_question.current(0)
        self.text_answer.delete(0, END)
    def register_data(self):
        if self.text_fname.get()=="" or self.text_lname.get()=="" or self.text_contact.get()=="" or self.text_email.get()=="" or self.cmb_question.get()=="select" or self.text_answer.get()=="" or self.text_password.get()=="" or self.text_cpassword.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        elif self.text_password.get()!=self.text_cpassword.get():
            messagebox.showerror("Error","Password & Confirm Password should be Same",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Please Agree Our Terms & Conditions",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="student")
                cur=con.cursor()
                cur.execute("select * from register where email=%s",self.text_email.get())
                row=cur.fetchone()
                #print(row)
                if row!=None:
                    messagebox.showerror("Error","User Already Exist, Please try with another Email",parent=self.root)

                else:
                    cur.execute("insert into register(f_name,l_name,contact,email,question,answer,password)values(%s,%s,%s,%s,%s,%s,%s)",
                            (self.text_fname.get(),
                             self.text_lname.get(),
                             self.text_contact.get(),
                             self.text_email.get(),
                             self.cmb_question.get(),
                             self.text_answer.get(),
                             self.text_password.get()
                             ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Register Successfull",parent=self.root)
                    self.root.destroy()
                    import studentlogin


            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)

root=Tk()
obj=register(root)
root.mainloop()