from tkinter import*
from PIL import ImageTk 
import dashboard

from userController import authenticate_user
from util.config import get_bg_image_url

class login:
    def __init__(self,db,root,disptext):
        self.disptext=disptext
        self.root=root
        self.db=db
        self.root.title("Login system")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(True,True)

        #====BG Image=====
        self.bg=ImageTk.PhotoImage(file=get_bg_image_url())
        self.bg_Image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1.3,relheight=1)
        
        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=150,y=150,height=340,width=500)

        title=Label(Frame_login,text="Login Here",font=("Impact",35,"bold"),fg="black",bg="white").place(x=90,y=30)
        desc=Label(Frame_login,text=disptext,font=("Goudy old style",15,"bold"),fg="black",bg="white").place(x=90,y=100)

        lbl_user=Label(Frame_login,text="User name",font=("Goudy old style",15,"bold"),fg="black",bg="white").place(x=90,y=140)
        self.txt_user=Entry(Frame_login,font=(" times new roman",15),bg="lightgray")
        self.txt_user.place(x=90,y=170,width=350,height=35)

        lbl_pass=Label(Frame_login,text="Password",font=("Goudy old style",15,"bold"),fg="black",bg="white").place(x=90,y=210)
        self.txt_pass=Entry(Frame_login,font=(" times new roman",15),bg="lightgray",show="*")
        self.txt_pass.place(x=90,y=240,width=350,height=35)

        Login_btn=Button(self.root,text="Login",fg="black",bg="white",font=("times new roman",20),command=self.dash).place(x=300,y=470,width=180,height=40)
    
    def dash(self):
        print(self.txt_user.get(),self.txt_pass.get())
        payload=authenticate_user(self.db,self.txt_user.get(),self.txt_pass.get())
        if(payload["status"]==200):
            print("Login Sucess")
            if(self.disptext=="Admin login area"):
                top=Toplevel()
                obj3=dashboard.adashboard(self.db,top,self)
                self.root.withdraw()
            elif(self.disptext=="Police login area"):
                top=Toplevel()
                obj3=dashboard.pdashboard(self.db,top,self)
                self.root.withdraw()
        else:
            print("Login Fail")
            Label(self.root,text="login fail",font=("Goudy old style",15,"bold"),fg="red",bg="white").place(x=300,y=100)


        