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

        frame1 = Frame(self.root, bg="#778beb")
        frame1.place(x=0, y=10, width=1550, height=130)

        frame1.Image = ImageTk.PhotoImage(file="images/logo.jpeg")
        frame1.Image_pack = Label(self.root, image=frame1.Image).place(x=230, y=5, width=1000, height=140)


        self.search_by=StringVar()
        self.search_text=StringVar()


        frame3 = Frame(self.root, bg="#fd79a8")
        frame3.place(x=50, y=150, width=1350, height=830)
        title = Label(frame3, text="Placed Students Record", font=("times new roman", 30, "bold"), bg="#778beb",fg="white").place(x=2, y=10, width=1400,height=40)


        btn_Search = Button(self.root, text="Search",command=self.search_data, font=("times new roman", 20), bd=2, cursor="hand2", bg="white",fg="black").place(x=700, y=210, width=120, height=30)
        btn_ShowAll = Button(self.root, text="Show All",command=self.fetch_data, font=("times new roman", 20), bd=2, cursor="hand2", bg="white",fg="black").place(x=850, y=210, width=120, height=30)
        btn_HomePage = Button(self.root, text="Home Page",command=self.HomePage_Window, font=("times new roman", 20), bd=2,cursor="hand2", bg="white", fg="black").place(x=1200, y=210, width=140, height=30)
        btn_ComPage = Button(self.root, text="Company Info.", command=self.Comapny_Window, font=("times new roman", 20), bd=2, cursor="hand2", bg="white", fg="black").place(x=1000, y=210, width=180, height=30)


        search = Label(frame3, text="Search:-", font=("times new roman", 20, "bold"), bg="#fd79a8", fg="white").place(x=140, y=55)
        self.cmb_search = ttk.Combobox(frame3,textvariable=self.search_by,text="Select Option", font=("times new roman", 13), state='readonly', justify=CENTER)
        self.cmb_search['values'] = ("Select Options", "Stu_Name")
        self.cmb_search.place(x=250, y=60,height=30)
        self.cmb_search.current(0)

        self.cmb_search = Entry(frame3,textvariable=self.search_text, font=("times new roman", 15), bg="white",bd=2)
        self.cmb_search.place(x=470, y=60, width=150, height=30)

        frame4=Frame(frame3,bd=4,relief=RIDGE,bg="#fd79a8")
        frame4.place(x=250, y=110, width=900, height=520)



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


        #self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()




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


    def Comapny_Window(self):
            self.root.destroy()
            import StuComView




root = Tk()
obj=step1(root)
root.mainloop()
