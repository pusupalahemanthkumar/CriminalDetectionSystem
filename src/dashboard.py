from tkinter import*
from PIL import ImageTk 
from tkinter import filedialog as fd
import os
import shutil
from faceRecognition import face_recognition
from faceRecognition import stop_recognition
from criminalController import get_criminal_tracker_data
from criminalController import add_criminal_location
from userController import register_user


class adashboard:
    def __init__(self,db,root,obj):
        self.root=root
        self.db=db
        self.root.title("Login system")
        self.obj=obj
        self.root.geometry("1600x800+100+50")
        self.root.resizable(True,True)

        #====BG Image=====
        #self.bg=ImageTk.PhotoImage(file="login.jpg")
        #self.bg_Image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=90,y=80,height=450,width=400)

        title=Label(Frame_login,text="Dashboard",font=("Impact",35,"bold"),fg="black",bg="white").place(x=90,y=30)

        lbl_user=Button(Frame_login,text="Users",font=("Goudy old style",20,"bold"),fg="black",bg="white",command=self.user).place(x=130,y=140)

        lbl_detections=Button(Frame_login,text="Detections",font=("Goudy old style",20,"bold"),fg="black",bg="white",command=self.detections).place(x=130,y=190)
        
        lbl_upload=Button(Frame_login,text="Upload",font=("Goudy old style",20,"bold"),fg="black",bg="white",command=self.upload).place(x=130,y=240)

        lbl_livecapture=Button(Frame_login,text="Live Capture",font=("Goudy old style",20,"bold"),fg="black",bg="white",command=self.livecapture).place(x=130,y=290)
        
        Logout_btn=Button(self.root,text="Logout",fg="black",bg="white",font=("times new roman",20),command=self.logout).place(x=190,y=470,width=180,height=40)
    def user(self):
        add_user=Button(self.root,text="Add user",font=("Goudy old style",25,"bold"),fg="black",bg="white",command=self.adduser).place(x=750,y=100,width=300,height=40)
    def detections(self):
        payload=get_criminal_tracker_data(self.db)
        print("------------ Detection Data----------------")
        print(payload)
        frame = Frame(self.root,bg='#A8B9BF').place(x=750,y=80,height=600,width=600)
        text_box = Text(self.root,height=600,width=600, font=(12),wrap=WORD)
        text_box.place(x=750,y=80,height=600,width=600)
        text_box.config(bg='#D9D8D7')
        sb = Scrollbar(self.root,orient=VERTICAL,command=text_box.yview)
        text_box['yscrollcommand'] = sb.set
        text_box.insert(END,"Detections:")
        for i in payload['data']:
            text_box.insert(END,"\n"+"Name:"+i['name']+"\t"+"Location:"+i['location']+"\t"+"Time:"+i['timestamp'].strftime("%d/%m/%Y %H:%M:%S")+"\t")

    def uploadfile(self):
        filename = fd.askopenfilenames(parent=self.root, title='Choose a file')
        print(filename)
        parent_dir = r"C:\Users\Welcome\Desktop\MiniProject\CriminalDetectionSystem\Resources\storage"
        path=os.path.join(parent_dir,self.uploadname.get())
        try: 
            os.mkdir(path) 
            for i in filename:
                shutil.copy(i, path)
            Label(self.root,text="uploading done",font=("Goudy old style",15,"bold"),fg="green",bg="white").place(x=650,y=100)
        except OSError as error: 
            print(error)
    def upload(self):
        upl=Label(self.root,text="Name:",font=("Impact",35,"bold"),fg="black",bg="white").place(x=750,y=200,width=300,height=40)
        self.uploadname=Entry(self.root,font=(" times new roman",15),bg="lightgray")
        self.uploadname.place(x=750,y=250,width=300,height=40)
        upload_btn=Button(self.root,text="Upload File",font=("Goudy old style",20,"bold"),fg="black",bg="white",command=self.uploadfile).place(x=750,y=300,width=300,height=40)
        
    def livecapture(self):
        print("--------------Started Face Recognition----------------")
        face_recognition(self.db)
    def logout(self):
        self.obj.root.deiconify()
        self.root.destroy()
    def adduser(self):
        Name=Label(self.root,text="Name:").place(x=750,y=130,width=300,height=40)
        self.name=Entry(self.root,font=(" times new roman",17),bg="lightgray")
        self.name.place(x=750,y=160,width=300,height=40)
        Email=Label(self.root,text="Email:").place(x=750,y=190,width=300,height=40)
        self.email=Entry(self.root,font=(" times new roman",17),bg="lightgray")
        self.email.place(x=750,y=220,width=300,height=40)
        Phone=Label(self.root,text="Phone:").place(x=750,y=250,width=300,height=40)
        self.phone=Entry(self.root,font=(" times new roman",17),bg="lightgray")
        self.phone.place(x=750,y=280,width=300,height=40)
        Password=Label(self.root,text="Password:").place(x=750,y=310,width=300,height=40)
        self.pwd=Entry(self.root,font=(" times new roman",17),bg="lightgray",show="*")
        self.pwd.place(x=750,y=340,width=300,height=40)
        Register=Button(self.root,text="Register",fg="black",bg="white",font=("times new roman",20),command=self.usereg)
        Register.place(x=750,y=370,width=300,height=40)
    def usereg(self):
        print(self.name.get(),self.email.get(),self.phone.get(),self.pwd.get())
        payload=register_user(self.db,self.name.get(),self.email.get(),self.pwd.get())
        Label(self.root,text="User added",font=("Goudy old style",17,"bold"),fg="green",bg="white").place(x=750,y=400)
        # if(payload["status"]==200):
        #     Label(self.root,text="Added User",font=("Goudy old style",15,"bold"),fg="red",bg="white").place(x=300,y=100)
        # else:
        #     Label(self.root,text="something went wrong",font=("Goudy old style",15,"bold"),fg="red",bg="white").place(x=300,y=100)


        print(payload)


class pdashboard:
    def __init__(self,db,root,obj):
        self.root=root
        self.db=db
        self.obj=obj
        self.root.title("Login system")
        self.root.geometry("1600x800+100+50")
        self.root.resizable(True,True)

        #====BG Image=====
        #self.bg=ImageTk.PhotoImage(file="login.jpg")
        #self.bg_Image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=90,y=80,height=450,width=400)

        title=Label(Frame_login,text="Dashboard",font=("Impact",35,"bold"),fg="black",bg="white").place(x=90,y=30)

        lbl_detections=Button(Frame_login,text="Detections",font=("Goudy old style",20,"bold"),fg="black",bg="white",command=self.detections).place(x=130,y=190)
        
        lbl_upload=Button(Frame_login,text="Upload",font=("Goudy old style",20,"bold"),fg="black",bg="white",command=self.upload).place(x=130,y=240)

        lbl_livecapture=Button(Frame_login,text="Live Capture",font=("Goudy old style",20,"bold"),fg="black",bg="white",command=self.livecapture).place(x=130,y=290)
        
        Logout_btn=Button(self.root,text="Logout",fg="black",bg="white",font=("times new roman",20),command=self.logout).place(x=190,y=470,width=180,height=40)
    
    def detections(self):
        payload=get_criminal_tracker_data(self.db)
        print("------------ Detection Data----------------")
        print(payload)
        frame = Frame(self.root,bg='#A8B9BF').place(x=750,y=80,height=600,width=600)
        text_box = Text(self.root,height=600,width=600, font=(12),wrap=WORD)
        text_box.place(x=750,y=80,height=600,width=600)
        text_box.config(bg='#D9D8D7')
        sb = Scrollbar(self.root,orient=VERTICAL,command=text_box.yview)
        text_box['yscrollcommand'] = sb.set
        text_box.insert(END,"Detections:")
        for i in payload['data']:
            text_box.insert(END,"\n"+"Name:"+i['name']+"\t"+"Location:"+i['location']+"\t"+"Time:"+i['timestamp'].strftime("%d/%m/%Y %H:%M:%S")+"\t")

    def uploadfile(self):
        filename = fd.askopenfilenames(parent=self.root, title='Choose a file')
        print(filename)
        parent_dir = r"C:\Users\kittu\Downloads\Project\CriminalDetectionSystem-main\Resources\storage"
        path=os.path.join(parent_dir,self.uploadname.get())
        try: 
            os.mkdir(path) 
            for i in filename:
                shutil.copy(i, path)
        except OSError as error: 
            print(error)
    def upload(self):
        upl=Label(self.root,text="Name:",font=("Impact",35,"bold"),fg="black",bg="white").place(x=750,y=200,width=300,height=40)
        self.uploadname=Entry(self.root,font=(" times new roman",15),bg="lightgray")
        self.uploadname.place(x=750,y=250,width=300,height=40)
        upload_btn=Button(self.root,text="Upload File",font=("Goudy old style",20,"bold"),fg="black",bg="white",command=self.uploadfile).place(x=750,y=300,width=300,height=40)
        
    def livecapture(self):
        print("--------------Started Face Recognition----------------")
        face_recognition(self.db)
    def logout(self):
        self.obj.root.deiconify()
        self.root.destroy()