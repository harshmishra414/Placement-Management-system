from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import pymysql
class step1:
    def __init__(self,root):
        self.root=root
        self.root.title("Students Record Liabrary")
        self.root.geometry("1550x800+0+0")
        #self.bg=ImageTk.PhotoImage(file="images/logo.jpeg")
        #self.bg_image=Label(self.frame1,image=self.bg).place(x=0,y=0)

        frame1 = Frame(self.root, bg="#b71540")
        frame1.place(x=0, y=10, width=1550, height=130)

        frame1.Image = ImageTk.PhotoImage(file="images/logo.jpeg")
        frame1.Image_pack = Label(self.root, image=frame1.Image).place(x=230, y=5, width=1000, height=140)

        frame2=Frame(self.root,bg="#079992")
        frame2.place(x=0 ,y=150 , width=550 , height=700)

        #----------ALL VARIABLES=========
        self.text_Stu_Name_var=StringVar()
        self.text_Branch_var=StringVar()
        self.text_E_mail_var=StringVar()
        self.text_Contact_var=StringVar()
        self.cmb_Gender_var=StringVar()
        self.text_Company_var=StringVar()
        self.text_Package_var=StringVar()
        self.search_by=StringVar()
        self.search_text=StringVar()

        title = Label(frame2, text="Company Reegistration", font=("times new roman", 30, "bold"), bg="#b71540", fg="white").place(x=0, y=10 ,width=550,height=40)


        Com_Name = Label(frame2, text="Comp_Name", font=("times new roman", 25, "bold"), bg="#079992", fg="white").place(x=30, y=60)
        self.text_Com_Name = Entry(frame2, font=("times new roman", 20), bg="white")
        self.text_Com_Name.place(x=250, y=70, width=290 , height=30)
        Reg_Num = Label(frame2, text="Regi_Number", font=("times new roman", 25, "bold"), bg="#079992", fg="white").place(x=30, y=110)
        self.text_Reg_Num = Entry(frame2, font=("times new roman", 20), bg="white")
        self.text_Reg_Num.place(x=250 , y=120, width=290, height=30)
        Year = Label(frame2, text="Year", font=("times new roman", 25, "bold"), bg="#079992", fg="white").place(x=30, y=170)
        self.text_Year = Entry(frame2, font=("times new roman", 20), bg="white")
        self.text_Year.place(x=250, y=180, width=290, height=30)
        Address = Label(frame2, text="Com_Address", font=("times new roman", 25, "bold"), bg="#079992", fg="white").place(x=30, y=230)
        self.text_Com_Address = Entry(frame2, font=("times new roman", 20), bg="white")
        self.text_Com_Address.place(x=250, y=240, width=290, height=30)

        title = Label(frame2, text="Company Criteria", font=("times new roman", 30, "bold"), bg="#b71540", fg="white").place(x=0, y=300 ,width=550,height=40)
        SSC = Label(frame2, text="10th(SSC)", font=("times new roman", 25, "bold"), bg="#079992", fg="white").place(x=30, y=350)
        self.text_SSC = Entry(frame2, font=("times new roman", 20), bg="white")
        self.text_SSC.place(x=250, y=360, width=290, height=30)
        HSC = Label(frame2, text="12th(HSC)", font=("times new roman", 25, "bold"), bg="#079992", fg="white").place(x=30, y=400)
        self.text_HSC = Entry(frame2, font=("times new roman", 20), bg="white")
        self.text_HSC.place(x=250, y=410, width=290, height=30)
        B_Tech = Label(frame2, text="B.Tech", font=("times new roman", 25, "bold"), bg="#079992", fg="white").place(x=30, y=450)
        self.text_B_Tech = Entry(frame2, font=("times new roman", 20), bg="white")
        self.text_B_Tech.place(x=250, y=460, width=290, height=30)
        MBA = Label(frame2, text="MBA", font=("times new roman", 25, "bold"), bg="#079992", fg="white").place(x=30, y=500)
        self.text_MBA = Entry(frame2, font=("times new roman", 20), bg="white")
        self.text_MBA.place(x=250, y=510, width=290, height=30)




        frame3 = Frame(self.root, bg="#3c6382")
        frame3.place(x=550, y=150, width=1000, height=830)
        title = Label(frame3, text="Company  Details", font=("times new roman", 30, "bold"), bg="#b71540",fg="white").place(x=2, y=10, width=1000,height=40)

        btn_Add = Button(self.root, text="Save",command=self.add_data, font=("times new roman", 20),bd=2, cursor="hand2",bg="#b71540",fg="white").place(x=50, y=720, width=80,height=40)
        btn_Update = Button(self.root, text="Correct",command=self.update_data,  font=("times new roman", 20),bd=2, cursor="hand2",bg="#b71540",fg="white").place(x=160, y=720, width=100 , height=40)
        btn_Delete = Button(self.root, text="Remove",command=self.delete_data, font=("times new roman", 20),bd=2, cursor="hand2",bg="#b71540",fg="white").place(x=300, y=720, width=100 , height=40)
        btn_Clear = Button(self.root, text="Reset",command=self.clear, font=("times new roman", 20),bd=2, cursor="hand2",bg="#b71540",fg="white").place(x=430, y=720, width=100 , height=40)
        btn_Search = Button(self.root, text="Search",command=self.search_data, font=("times new roman", 20), bd=2, cursor="hand2", bg="white",fg="black").place(x=1080, y=210, width=120, height=30)
        btn_ShowAll = Button(self.root, text="Show All",command=self.fetch_data, font=("times new roman", 20), bd=2, cursor="hand2", bg="white",fg="black").place(x=1230, y=210, width=120, height=30)
        btn_HomePage = Button(self.root, text="Home Page",command=self.HomePage_Window, font=("times new roman", 20), bd=2,cursor="hand2", bg="white", fg="black").place(x=1380, y=210, width=140, height=30)




        #Search = Label(frame3, text="Students Data", font=("times new roman", 30, "bold")).place(x=0, y=50, width=550, height=40)
        #title = Label(frame3, text="Search By", font=("times new roman", 20, "bold"),bg="#fd79a8").place(x=20, y=55)

        search = Label(frame3, text="Search:-", font=("times new roman", 20, "bold"), bg="#3c6382", fg="white").place(x=20, y=55)
        self.cmb_search = ttk.Combobox(frame3,textvariable=self.search_by,text="Select Option", font=("times new roman", 13), state='readonly', justify=CENTER)
        self.cmb_search['values'] = ("Select Options", "Com_Name")
        self.cmb_search.place(x=120, y=60,height=30)
        self.cmb_search.current(0)

        self.cmb_search = Entry(frame3,textvariable=self.search_text, font=("times new roman", 15), bg="white",bd=2)
        self.cmb_search.place(x=350, y=60, width=150, height=30)

        frame4=Frame(frame3,bd=4,relief=RIDGE,bg="#fd79a8")
        frame4.place(x=40, y=110, width=900, height=520)



        scroll_x=Scrollbar(frame4,orient=HORIZONTAL)
        scroll_y = Scrollbar(frame4,orient=VERTICAL)

        self.student_table=ttk.Treeview(frame4,columns=("Com_Name","Regi_Number","Year","Com_Address","10th(SSC)","12th(HSC)","B_Tech","MBA"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview_scroll)
        scroll_y.config(command=self.student_table.yview_scroll)

        self.student_table.heading("Com_Name",text="Com_Name")
        self.student_table.heading("Regi_Number", text="Regi_Number")
        self.student_table.heading("Year", text="Year")
        self.student_table.heading("Com_Address", text="Com_Address")
        self.student_table.heading("10th(SSC)", text="10th(SSC)")
        self.student_table.heading("12th(HSC)", text="12th(HSC)")
        self.student_table.heading("B_Tech", text="B_Tech")
        self.student_table.heading("MBA", text="MBA")
        self.student_table['show']='headings'
        self.student_table.column("Com_Name", width=150)
        self.student_table.column("Regi_Number", width=80)
        self.student_table.column("Year", width=70)
        self.student_table.column("Com_Address", width=200)
        self.student_table.column("10th(SSC)",width=60)
        self.student_table.column("12th(HSC)", width=60)
        self.student_table.column("B_Tech", width=60)
        self.student_table.column("MBA", width=60)
        self.student_table.pack(fill=BOTH,expand=0.5)


        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()



    def clear(self):
        self.text_Com_Name.delete(0,END)
        self.text_Reg_Num.delete(0, END)
        self.text_Year.delete(0, END)
        self.text_Com_Address.delete(0, END)
        self.text_SSC.delete(0,END)
        self.text_HSC.delete(0, END)
        self.text_B_Tech.delete(0,END)
        self.text_MBA.delete(0,END)

        #self.text_answer.delete(0, END)

    def add_data(self):
        if self.text_Com_Name.get()=="" or self.text_Reg_Num.get()=="" or self.text_Year.get()=="" or self.text_Com_Address.get()=="" or self.text_SSC.get()=="" or  self.text_HSC.get()=="" or self.text_B_Tech.get()=="" or self.text_MBA.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        #elif self.text_password.get()!=self.text_cpassword.get():
            #messagebox.showerror("Error","Password & Confirm Password should be Same",parent=self.root)
        #elif self.var_chk.get()==0:
            #messagebox.showerror("Error","Please Agree Our Terms & Conditions",parent=self.root)

        else:

            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="student")
                cur=con.cursor()
                cur.execute("INSERT INTO Company values(%s,%s,%s,%s,%s,%s,%s,%s)",
                        (self.text_Com_Name.get(),
                         self.text_Reg_Num.get(),
                         self.text_Year.get(),
                         self.text_Com_Address.get(),
                         self.text_SSC.get(),
                         self.text_HSC.get(),
                         self.text_B_Tech.get(),
                         self.text_MBA.get()

                        ))

                con.commit()
                self.fetch_data()
                self.clear()
                messagebox.showinfo("Added", "Data Added Successfully", parent=self.root)
                con.close()

            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)



    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="student")
        cur = con.cursor()
        cur.execute("select * from Company")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
            con.commit()
        con.close()


    def get_cursor(self,ev):
        curosor_row=self.student_table.focus()
        contents=self.student_table.item(curosor_row)
        row=contents['values']
        print(row)
        self.text_Com_Name.delete("1",END)
        self.text_Com_Name.insert(END,row[0])
        self.text_Reg_Num.delete("2",END)
        self.text_Reg_Num.insert(END,row[1])
        self.text_Year.delete("3",END)
        self.text_Year.insert(END,row[2])
        self.text_Com_Address.delete("4",END)
        self.text_Com_Address.insert(END,row[3])
        self.text_SSC.delete("5",END)
        self.text_SSC.insert(END,row[4])
        self.text_HSC.delete("6",END)
        self.text_HSC.insert(END,row[5])
        self.text_B_Tech.delete("7",END)
        self.text_B_Tech.insert(END,row[6])
        self.text_MBA.delete("8",END)
        self.text_MBA.insert(END,row[7])


        '''con = pymysql.connect(host="localhost", user="root", password="", database="student")
        cur = con.cursor()
        cur.execute("select * from data where E_mail=%s")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('', END, values=row)
            con.commit()
        con.close()'''

    def update_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="student")
        cur = con.cursor()
        cur.execute("UPDATE Company SET Com_Name=%s,Year=%s,Com_Address=%s,SSC=%s, HSC=%s, B_Tech=%s, MBA=%s where Reg_Number=%s",
                    (self.text_Com_Name.get(),
                     self.text_Year.get(),
                     self.text_Com_Address.get(),
                     self.text_SSC.get(),
                     self.text_HSC.get(),
                     self.text_B_Tech.get(),
                     self.text_MBA.get(),
                     self.text_Reg_Num.get(),
                     ))

        con.commit()
        self.fetch_data()
        self.clear()
        messagebox.showinfo("Added", "Data Added Successfully", parent=self.root)
        con.close()

    def delete_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="student")
        cur = con.cursor()
        cur.execute("delete from Company where Reg_Number=%s",self.text_Reg_Num.get())

        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    def search_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="student")
        cur = con.cursor()

        cur.execute("select * from Company where Com_Name=%s",(str(self.search_text.get())))
        rows=cur.fetchall()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('', END, values=row)

            con.commit()
        con.close()

    def HomePage_Window(self):
            self.root.destroy()
            import FrontPage




root = Tk()
obj=step1(root)
root.mainloop()
