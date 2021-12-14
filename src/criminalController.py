import datetime
import pprint
from util.db_conn import connect_db

def get_criminal_tracker_data(db):
    criminal_tracker=db["criminalTracker"]
    try:
        data= criminal_tracker.find({})
        criminal=[]
        for i in data:
            criminal.append(i)
            print(i)
        payload={"message":"Sucess","status":200,"data":criminal}
        return payload
    except Exception:
        print("-------Something Went Wrong!--------")

def add_criminal_location(db,name,location):
    criminal_tracker=db["criminalTracker"]
    try:
        criminal_trace_id= criminal_tracker.insert_one({"name":name,"location":location,"timestamp":datetime.datetime.now()})
        if(criminal_trace_id):
            payload={"message":"success","status":200}
            return payload
    except Exception:
        print("-------Something Went Wrong--------")




