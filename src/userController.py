from util.db_conn import connect_db

def authenticate_user(db,email,password):
    users=db["users"]
    is_valid_user= users.find_one({"email":email,"password":password})

    if(is_valid_user==None):
        payload={"message":"Invlaid email or password","status":500}
        return payload
    else:
        payload={"message":"success","status":200,"user":is_valid_user}
        return payload

def register_user(db,name,email,password):
    users=db["users"]
    try:
        register_id=users.insert_one({"name":name,"email":email,"password":password})
        if(register_id):
            print(register_id)
            payload={"message":"success","status":200}
    except Exception:
        print("unable to insert user data")








