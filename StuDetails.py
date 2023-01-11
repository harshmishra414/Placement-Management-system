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

        frame1 = Frame(self.root, bg="navy blue")
        frame1.place(x=0, y=10, width=1550, height=130)

        frame1.Image = ImageTk.PhotoImage(file="images/logo.jpeg")
        frame1.Image_pack = Label(self.root, image=frame1.Image).place(x=230, y=5, width=1000, height=140)

        frame2=Frame(self.root,bg="#10ac84")
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

        title = Label(frame2, text="Students Data", font=("times new roman", 30, "bold"), bg="navy blue", fg="white").place(x=0, y=10 ,width=550,height=40)


        Stu_Name = Label(frame2, text="Stu_Name", font=("times new roman", 25, "bold"), bg="#10ac84", fg="white").place(x=30, y=110)
        self.text_Stu_Name = Entry(frame2, font=("times new roman", 20), bg="white")
        self.text_Stu_Name.place(x=250, y=110, width=290 , height=30)
        Branch = Label(frame2, text="Branch", font=("times new roman", 25, "bold"), bg="#10ac84", fg="white").place(x=30, y=170)
        self.text_Branch = Entry(frame2, font=("times new roman", 20), bg="white")
        self.text_Branch.place(x=250 , y=170, width=290, height=30)
        E_mail = Label(frame2, text="E_mail", font=("times new roman", 25, "bold"), bg="#10ac84", fg="white").place(x=30, y=220)
        self.text_E_mail = Entry(frame2, font=("times new roman", 20), bg="white")
        self.text_E_mail.place(x=250, y=220, width=290, height=30)
        Contact = Label(frame2, text="Contact", font=("times new roman", 25, "bold"), bg="#10ac84", fg="white").place(x=30, y=280)
        self.text_Contact = Entry(frame2, font=("times new roman", 20), bg="white")
        self.text_Contact.place(x=250, y=280, width=290, height=30)
        '''Gender = Label(frame2, text="Gender", font=("times new roman", 25, "bold"), bg="#10ac84", fg="white").place(x=30, y=350)
        self.text_Gender = Entry(frame2, font=("times new roman", 20), bg="white")
        self.text_Gender.place(x=250, y=350, width=290, height=30)'''
        Gender = Label(frame2, text="Gender", font=("times new roman", 20, "bold"), bg="#10ac84",fg="white").place(x=30, y=350)
        self.cmb_Gender = ttk.Combobox(frame2, font=("times new roman", 13), state='readonly', justify=CENTER)
        self.cmb_Gender['values'] = ("Select", "Male", "Female", "Other")
        self.cmb_Gender.place(x=250, y=350, width=250)
        self.cmb_Gender.current(0)
        #answer = Label(frame1, text="Answer", font=("times new roman", 20, "bold"), bg="white", fg="gray").place(x=30, y=240)
        #self.text_answer = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        #self.text_answer.place(x=250, y=350, width=290,height=30)
        Company = Label(frame2, text="Company", font=("times new roman", 25, "bold"), bg="#10ac84", fg="white").place(x=30, y=410)
        self.text_Company = Entry(frame2, font=("times new roman", 20), bg="white")
        self.text_Company.place(x=250, y=410, width=290, height=30)
        Package = Label(frame2, text="Package", font=("times new roman", 25, "bold"), bg="#10ac84", fg="white").place(x=30, y=460)
        self.text_Package = Entry(frame2, font=("times new roman", 20), bg="white")
        self.text_Package.place(x=250, y=460, width=290, height=30)

        frame3 = Frame(self.root, bg="#1dd1a1")
        frame3.place(x=550, y=150, width=1000, height=830)
        title = Label(frame3, text="Placed Students Record", font=("times new roman", 30, "bold"), bg="navy blue",fg="white").place(x=2, y=10, width=1000,height=40)

        btn_Add = Button(self.root, text="Add",command=self.add_data, font=("times new roman", 20),bd=2, cursor="hand2",bg="#5f27cd",fg="white").place(x=50, y=670, width=80,height=40)
        btn_Update = Button(self.root, text="Update",command=self.update_data,  font=("times new roman", 20),bd=2, cursor="hand2",bg="#5f27cd",fg="white").place(x=160, y=670, width=100 , height=40)
        btn_Delete = Button(self.root, text="Delete",command=self.delete_data, font=("times new roman", 20),bd=2, cursor="hand2",bg="#5f27cd",fg="white").place(x=300, y=670, width=100 , height=40)
        btn_Clear = Button(self.root, text="Clear",command=self.clear, font=("times new roman", 20),bd=2, cursor="hand2",bg="#5f27cd",fg="white").place(x=430, y=670, width=100 , height=40)
        btn_Search = Button(self.root, text="Search",command=self.search_data, font=("times new roman", 20), bd=2, cursor="hand2", bg="white",fg="navy blue").place(x=1080, y=210, width=120, height=30)
        btn_ShowAll = Button(self.root, text="Show All",command=self.fetch_data, font=("times new roman", 20), bd=2, cursor="hand2", bg="white",fg="navy blue").place(x=1230, y=210, width=120, height=30)
        btn_HomePage = Button(self.root, text="Home Page",command=self.HomePage_Window, font=("times new roman", 20), bd=2,cursor="hand2", bg="white", fg="navy blue").place(x=1380, y=210, width=140, height=30)
        btn_Company = Button(self.root, text="Company Details", command=self.Company_Window, font=("times new roman", 20), bd=2, cursor="hand2", bg="light green", fg="navy blue").place(x=170, y=730, width=200, height=40)



        #Search = Label(frame3, text="Students Data", font=("times new roman", 30, "bold")).place(x=0, y=50, width=550, height=40)
        #title = Label(frame3, text="Search By", font=("times new roman", 20, "bold"),bg="#fd79a8").place(x=20, y=55)

        search = Label(frame3, text="Search:-", font=("times new roman", 20, "bold"), bg="#1dd1a1", fg="white").place(x=20, y=55)
        self.cmb_search = ttk.Combobox(frame3,textvariable=self.search_by,text="Select Option", font=("times new roman", 13), state='readonly', justify=CENTER)
        self.cmb_search['values'] = ("Select Options", "Stu_Name")
        self.cmb_search.place(x=120, y=60,height=30)
        self.cmb_search.current(0)

        self.cmb_search = Entry(frame3,textvariable=self.search_text, font=("times new roman", 15), bg="white",bd=2)
        self.cmb_search.place(x=350, y=60, width=150, height=30)

        frame4=Frame(frame3,bd=4,relief=RIDGE,bg="Red")
        frame4.place(x=40, y=110, width=900, height=520)



        scroll_x=Scrollbar(frame4,orient=HORIZONTAL)
        scroll_y = Scrollbar(frame4,orient=VERTICAL)

        self.student_table=ttk.Treeview(frame4,columns=("Stu_Name","Branch","E_mail","Contact","Gender","Company","Package"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview_scroll)
        scroll_y.config(command=self.student_table.yview_scroll)

        self.student_table.heading("Stu_Name",text="Stu_Name")
        self.student_table.heading("Branch", text="Branch")
        self.student_table.heading("E_mail", text="E_mail")
        self.student_table.heading("Contact", text="Contact")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("Company", text="Company")
        self.student_table.heading("Package", text="Package")
        self.student_table['show']='headings'
        self.student_table.column("Stu_Name", width=170)
        self.student_table.column("Branch", width=60)
        self.student_table.column("E_mail", width=210)
        self.student_table.column("Contact", width=80)
        self.student_table.column("Gender",width=60)
        self.student_table.column("Company", width=150)
        self.student_table.column("Package", width=110)
        self.student_table.pack(fill=BOTH,expand=0.5)


        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()



    def clear(self):
        self.text_Stu_Name.delete(0,END)
        self.text_Branch.delete(0, END)
        self.text_E_mail.delete(0, END)
        self.text_Contact.delete(0, END)
        self.text_Company.delete(0,END)
        self.text_Package.delete(0, END)
        self.cmb_Gender.current(0)
        #self.text_answer.delete(0, END)

    def add_data(self):
        if self.text_Stu_Name.get()=="" or self.text_Branch.get()=="" or self.text_E_mail.get()=="" or self.text_Company.get()=="" or self.cmb_Gender.get()=="select" or  self.text_Package.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:

            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="student")
                cur=con.cursor()
                cur.execute("INSERT INTO data values(%s,%s,%s,%s,%s,%s,%s)",
                        (self.text_Stu_Name.get(),
                         self.text_Branch.get(),
                         self.text_E_mail.get(),
                         self.text_Contact.get(),
                         self.cmb_Gender.get(),
                         self.text_Company.get(),
                         self.text_Package.get()
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
        cur.execute("select * from data")
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
        self.text_Stu_Name.delete("1",END)
        self.text_Stu_Name.insert(END,row[0])
        self.text_Branch.delete("2",END)
        self.text_Branch.insert(END,row[1])
        self.text_E_mail.delete("3",END)
        self.text_E_mail.insert(END,row[2])
        self.text_Contact.delete("4",END)
        self.text_Contact.insert(END,row[3])
        self.cmb_Gender.delete("5",END)
        self.cmb_Gender.insert(END,row[4])
        self.text_Company.delete("6",END)
        self.text_Company.insert(END,row[5])
        self.text_Package.delete("7",END)
        self.text_Package.insert(END,row[6])

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
        cur.execute("UPDATE data SET Stu_Name=%s,Branch=%s,Contact=%s,Gender=%s,Company=%s,Package=%s where E_mail=%s",
                    (self.text_Stu_Name.get(),
                     self.text_Branch.get(),
                     self.text_Contact.get(),
                     self.cmb_Gender.get(),
                     self.text_Company.get(),
                     self.text_Package.get(),
                     self.text_E_mail.get()
                     ))

        con.commit()
        self.fetch_data()
        self.clear()
        messagebox.showinfo("Added", "Data Added Successfully", parent=self.root)
        con.close()

    def delete_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="student")
        cur = con.cursor()
        cur.execute("delete from data where E_mail=%s",self.text_E_mail.get())

        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    def search_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="student")
        cur = con.cursor()

        cur.execute("select * from data where Stu_Name=%s",(str(self.search_text.get())))
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

    def Company_Window(self):
            self.root.destroy()
            import ComReg



root = Tk()
obj=step1(root)
root.mainloop()
