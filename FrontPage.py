from tkinter import *
from PIL import Image, ImageTk


class Front:
    def __init__(self, root):
        self.root = root
        self.root.title("Placement Management System")
        self.root.geometry("1600x900+0+0")

        # ======BackGround Colour==========

        self.bg = ImageTk.PhotoImage(file="images/567.jpg")

        # =====Put the Head Title=======
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # Creating object of photoimage class
        p1 = PhotoImage(file='images/1.png')

        # Setting icon of root window
        root.iconphoto(False, p1)

        # ========FRAME=====
        frame1 = Frame(self.root, bg="#00cec9")
        frame1.place(x=330, y=150, width=950, height=490)

        frame1.Image = ImageTk.PhotoImage(file="images/side1.jpeg")
        frame1.Image_pack = Label(self.root, image=frame1.Image).place(x=320, y=150)

        title = Label(frame1, text="Continue as ....", font=("times new roman", 55, "bold"), fg="white",bg="#00cec9").place(x=450, y=60)

        title = Label(text="Shree L R Tiwari College Of Engineering", font=("Goudy old style", 30, "bold"), fg="white",bg="#1d4e89").place(x=0, y=30, width=1550)

        Student = Button(frame1, text="Student", command=self.Student_window, font=("Goudy old style", 40),bg="navy blue", fg="white").place(x=420, y=150, width=530, heigh=70)

        title = Label(frame1, text="Or", font=("times new roman", 55, "bold"), fg="white", bg="#00cec9").place(x=620,y=225)

        Student = Button(frame1, text="College Dept.", command=self.College_window, font=("Goudy old style", 40),bg="navy blue", fg="white").place(x=400, y=330, width=550, heigh=70)

    # ==========Connnecting The Pages=========

    def Student_window(self):
        self.root.destroy()
        import studentlogin

    def College_window(self):
        self.root.destroy()
        import ClgLogin


root = Tk()
obj = Front(root)
root.mainloop()
