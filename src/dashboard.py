from tkinter import*
from PIL import ImageTk 
from tkinter import filedialog as fd

from faceRecognition import face_recognition
from faceRecognition import stop_recognition
from criminalController import get_criminal_tracker_data
from criminalController import add_criminal_location


class adashboard:
    def __init__(self,db,root,obj):
        self.root=root
        self.db=db
        self.root.title("Login system")
        self.obj=obj
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False,False)

        #====BG Image=====
        #self.bg=ImageTk.PhotoImage(file="login.jpg")
        #self.bg_Image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=90,y=80,height=450,width=400)

        title=Label(Frame_login,text="Dashboard",font=("Impact",35,"bold"),fg="black",bg="white").place(x=90,y=30)

        lbl_user=Button(Frame_login,text="Users",font=("Goudy old style",20,"bold"),fg="white",bg="black",command=self.user).place(x=130,y=140)

        lbl_detections=Button(Frame_login,text="Detections",font=("Goudy old style",20,"bold"),fg="black",bg="white",command=self.detections).place(x=130,y=190)
        
        lbl_upload=Button(Frame_login,text="Upload",font=("Goudy old style",20,"bold"),fg="black",bg="white",command=self.upload).place(x=130,y=240)

        lbl_livecapture=Button(Frame_login,text="Live Capture",font=("Goudy old style",20,"bold"),fg="black",bg="white",command=self.livecapture).place(x=130,y=290)
        
        Logout_btn=Button(self.root,text="Logout",fg="black",bg="white",font=("times new roman",20),command=self.logout).place(x=190,y=470,width=180,height=40)
    def user(self):
        add_user=Button(self.root,text="Add user",font=("Goudy old style",25,"bold"),fg="black",bg="white",command=self.adduser).place(x=750,y=200,width=300,height=40)
    def detections(self):
        payload=get_criminal_tracker_data(self.db)
        print("------------ Detection Data----------------")
        print(payload)
    def uploadfile(self):
        filename = fd.askopenfilename(initialdir='/',title="select a file to encrypt:",filetypes=(("Jpeg","*.jpg"),("all files","*.*")))
        print(filename)
    def upload(self):
        upload_btn=Button(self.root,text="Upload File",font=("Goudy old style",20,"bold"),fg="black",bg="white",command=self.uploadfile).place(x=750,y=200,width=300,height=40)
    def livecapture(self):
        print("--------------Started Face Recognition----------------")
        face_recognition(self.db)
    def logout(self):
        self.obj.root.deiconify()
        self.root.destroy()

    def adduser(self):
        pass

class pdashboard:
    def __init__(self,db,root,obj):
        self.root=root
        self.db=db
        self.root.title("Login system")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False,False)

        #====BG Image=====
        #self.bg=ImageTk.PhotoImage(file="login.jpg")
        #self.bg_Image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=90,y=80,height=450,width=400)

        title=Label(Frame_login,text="Dashboard",font=("Impact",35,"bold"),fg="black",bg="white").place(x=90,y=30)

        lbl_detections=Button(Frame_login,text="Detections",font=("Goudy old style",20,"bold"),fg="black",bg="white",command=self.detections).place(x=130,y=190)
        
        lbl_upload=Button(Frame_login,text="Upload",font=("Goudy old style",20,"bold"),fg="black",bg="white",command=self.upload).place(x=130,y=240)

        lbl_livecapture=Button(Frame_login,text="Live Capture",font=("Goudy old style",20,"bold"),fg="black",bg="white",command=self.livecapture).place(x=130,y=290)
        
        Logout_btn=Button(self.root,text="Logout",fg="black",bg="white",font=("times new roman",20)).place(x=190,y=470,width=180,height=40)
    
    def detections(self):
        payload=get_criminal_tracker_data(self.db)
        print("------------ Detection Data----------------")
        print(payload)
    def uploadfile(self):
        filename = fd.askopenfilename(initialdir='/',title="select a file to encrypt:",filetypes=(("Jpeg","*.jpg"),("all files","*.*")))
        print(filename)
    def upload(self):
        upload_btn=Button(self.root,text="Upload File",font=("Goudy old style",20,"bold"),fg="black",bg="white",command=self.uploadfile).place(x=750,y=200,width=300,height=40)
    def livecapture(self):
        print("--------------Started Face Recognition----------------")
        face_recognition(self.db)
    def logout(self):
        self.obj.root.deiconify()
        self.root.destroy()