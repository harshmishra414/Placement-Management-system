from tkinter import *
import qrcode
from PIL import Image,ImageTk
from resizeimage import  resizeimage
class QR_generator:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1520x800+0+0")
        self.root.title("QR Generator |  Developed By Suraj ")
        self.root.resizable(False,False)


        title=Label(self.root,text="QR code Generator",font=("times new roman",40),bg="#053246",fg="white").place(x=0,y=20,width=1530)

        #========Student Detail Window========

        self.var_Seat_Num=StringVar()
        self.var_Student_Name = StringVar()
        self.var_Branch = StringVar()
        self.var_Date_Of_Birth = StringVar()
        self.var_Mothers_Name = StringVar()
        self.var_SSC_Percentage = StringVar()
        self.var_HSC_Percentage = StringVar()
        self.var_3rd_Year_CGPA = StringVar()

        Stu_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Stu_Frame.place(x=150,y=150,width=700,height=600)

        Stu_title = Label(Stu_Frame, text="Student Details", font=("goudy old style", 40), bg="#043256",fg="white").place(x=0, y=0, width=700)


        lbl_Seat_Number = Label(Stu_Frame, text="Seat Number", font=("times new roman", 20,"bold"), bg="white",fg="Black").place(x=35, y=100)
        lbl_Student_Name = Label(Stu_Frame, text="Student Name", font=("times new roman", 20,"bold"), bg="white",fg="black").place(x=35, y=150)
        Stu_Branch = Label(Stu_Frame, text="Branch", font=("times new roman", 20,"bold"), bg="white",fg="black").place(x=34, y=200)
        Stu_Date_Of_Birth = Label(Stu_Frame, text="Date Of Birth", font=("times new roman", 20,"bold"), bg="white",fg="black").place(x=35, y=250)
        Stu_Mothers_Name = Label(Stu_Frame, text="Mothers Name", font=("times new roman", 20,"bold"), bg="white",fg="black").place(x=35, y=300)
        Stu_SSC_Percentage = Label(Stu_Frame, text="SSC Percentage", font=("times new roman", 20,"bold"), bg="white", fg="black").place(x=35,y=350)
        Stu_HSC_Percentage = Label(Stu_Frame, text="HSC Percentage", font=("times new roman", 20,"bold"), bg="white",fg="black").place(x=35, y=400)
        Stu_3rd_Year_CGPA = Label(Stu_Frame, text="3rd Year CGPA", font=("times new roman", 20,"bold"), bg="white",fg="black").place(x=35, y=450)

        txt_Seat_Number = Entry(Stu_Frame,font=("times new roman", 20),textvariable=self.var_Seat_Num, bg="light yellow").place(x=350, y=100)
        txt_Student_Name = Entry(Stu_Frame,font=("times new roman", 20),textvariable=self.var_Student_Name, bg="light yellow").place(x=350, y=150)
        txt_Branch = Entry(Stu_Frame,font=("times new roman", 20),textvariable=self.var_Branch, bg="light yellow").place(x=350, y=200)
        txt_Date_Of_Birth = Entry(Stu_Frame,font=("times new roman", 20),textvariable=self.var_Date_Of_Birth, bg="light yellow").place(x=350, y=250)
        txt_Mothers_Name = Entry(Stu_Frame,font=("times new roman", 20),textvariable=self.var_Mothers_Name, bg="light yellow").place(x=350, y=300)
        txt_SSC_Percentage = Entry(Stu_Frame,font=("times new roman", 20),textvariable=self.var_SSC_Percentage, bg="light yellow").place(x=350, y=350)
        txt_HSC_Percentage = Entry(Stu_Frame,font=("times new roman", 20),textvariable=self.var_HSC_Percentage, bg="light yellow").place(x=350, y=400)
        txt_3rd_Year_CGPA = Entry(Stu_Frame,font=("times new roman", 20),textvariable=self.var_3rd_Year_CGPA, bg="light yellow").place(x=350, y=450)


        btn_generate=Button(Stu_Frame,text="Generate QR",command=self.generate,font=("times new roman",18,"bold"),bg="#2196f3",fg="white").place(x=150,y=500,width=240,height=40)

        btn_clear = Button(Stu_Frame,command=self.clear, text="Clear", font=("times new roman", 18, "bold"), bg="#607d8b",fg="white").place(x=400, y=500, width=150, height=40)

        self.msg=""
        self.lbl_msg=Label(Stu_Frame, text=self.msg, font=("times new roman", 20), bg="white",fg="green")
        self.lbl_msg.place(x=160, y=550)

        # ========Student QR Frame Window========

        QR_Frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        QR_Frame.place(x=900, y=150, width=470, height=600)

        qr_code = Label(QR_Frame, text="QR Code Window", font=("goudy old style", 40), bg="#043256",fg="white").place(x=0, y=0, width=470)

        self.qr_code=Label(QR_Frame,text="No QR\n Available",font=("times new roman",25),bg="#3f51b5",fg="white")
        self.qr_code.place(x=80,y=140,width=300,height=300)

    def clear(self):
        self.var_Seat_Num.set("")
        self.var_Student_Name.set("")
        self.var_Branch.set("")
        self.var_Date_Of_Birth.set("")
        self.var_Mothers_Name.set("")
        self.var_SSC_Percentage.set("")
        self.var_HSC_Percentage.set("")
        self.var_3rd_Year_CGPA.set("")

        self.msg = ""
        self.lbl_msg.config(text=self.msg, fg="red")

        self.qr_code.config(image="")


    def generate(self):
        if self.var_Seat_Num.get()=="" or self.var_Student_Name.get()=="" or self.var_Branch.get()=="" or self.var_Mothers_Name.get()=="" or self.var_Date_Of_Birth.get()=="" or self.var_SSC_Percentage.get()=="" or self.var_HSC_Percentage.get()=="" or self.var_3rd_Year_CGPA.get()=="":
            self.msg="All Fields are Required!!!"
            self.lbl_msg.config(text=self.msg,fg="red")
        else:
            qr_data=(f"Seat_Num:{self.var_Seat_Num.get()}\nStudent_Name:{self.var_Student_Name.get()}\nBranch:{self.var_Branch.get()}\nMother_Name:{self.var_Mothers_Name.get()}\nDate_Of_Birth:{self.var_Date_Of_Birth.get()}\nSSC_Percentage:{self.var_SSC_Percentage.get()}\nHSC_Percentage:{self.var_HSC_Percentage.get()}\n3rd_Year_CGPA:{self.var_3rd_Year_CGPA.get()}")
            qr_code_run=qrcode.make(qr_data)
            #print(qr_code_run)
            qr_code_run=resizeimage.resize_cover(qr_code_run,[265,265])
            qr_code_run.save("Student_QR/Stu_"+str(self.var_Seat_Num.get())+'.png')
            #=======Code Image Update======
            self.im=ImageTk.PhotoImage(file="Student_QR/Stu_"+str(self.var_Seat_Num.get())+'.png')
            self.qr_code.config(image=self.im)
            self.msg = "QR Generated Successfully!!!"
            self.lbl_msg.config(text=self.msg, fg="green")





root=Tk()
obj = QR_generator(root)
root.mainloop()