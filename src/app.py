from util.db_conn import connect_db
from userController import authenticate_user
from userController import register_user
from criminalController import get_criminal_tracker_data
from criminalController import add_criminal_location
db=connect_db()

print("-------WELCOME TO THE PYTHON UTIL PROJECT---------\n")
choice=True

while choice:
    print("------Choose The Option Below------")
    print("1. create user")
    print("2. login user")
    print("3. get tracker data")
    print("4. add criminal location")
    print("5. exist ")
    op=int(input())
    if(op==1):
        print("Name : ")
        name=input()
        print("Email : ")
        email=input()
        print("Password : ")
        password=input()
        data=register_user(db,name,email,password)
        print(data)
    elif(op==2):
        print("Email : ")
        email=input()
        print("Password : ")
        password=input()
        data=authenticate_user(db,email,password)
        print(data)
    elif(op==3):
        data=get_criminal_tracker_data(db)
        print(data)
    elif(op==4):
        print("Criminal Name :")
        name=input()
        location=input()
        data=add_criminal_location(db,name,location)
        print(data)
    else:
        choice=False



