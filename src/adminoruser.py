from tkinter import*
from PIL import ImageTk
import login

from util.db_conn import connect_db
db=connect_db()

class adminoruser:
    def __init__(self,root):
        self.root=root
        self.root.title("Login system")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False,False)

        #====BG Image=====
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Welcome\Desktop\MiniProject\ScamProject\Resources\images\login.jpg")
        self.bg_Image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1.3,relheight=1)
        admin_btn=Button(self.root,text="Admin",fg="black",bg="white",font=("times new roman",20,"bold"),command=adlog).place(x=90,y=210,width=180,height=40)
        user_btn=Button(self.root,text="User",fg="black",bg="white",font=("times new roman",20,"bold"),command=log).place(x=90,y=280,width=180,height=40)
def adlog():
    obj2=login.login(db,root,disptext="Admin login area")
def log():
    obj2=login.login(db,root,disptext="Police login area")
root=Tk()
obj=adminoruser(root)
root.mainloop()