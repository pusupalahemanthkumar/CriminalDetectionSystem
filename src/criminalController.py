import datetime
import pprint
from util.db_conn import connect_db
from util.mailer import Mailer
from datetime import datetime

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


def add_criminal(db,name,crimate_rate):
    criminal=db["criminal"]
    try:
        criminal_id=criminal.insert_one({"name":name,"crimate_rate":crimate_rate})
        if(criminal_id):
            print(criminal_id)
            payload={"message":"success","status":200}
    except Exception:
        print("unable to add criminal data")

def add_criminal_location(db,name,location):
    criminal_tracker=db["criminalTracker"]
    try:
        print("in add c loca-1")
        criminal_trace_id= criminal_tracker.insert_one({"name":name,"location":location,"date":str(datetime.today().strftime('%Y-%m-%d')),"timestamp":datetime.now()})
        print("in add c loca-2")
        if(criminal_trace_id):
            print("in add c loca-3")
            if(criminal_tracker.find_one({"name":name,"location":location,"date":str(datetime.today().strftime('%Y-%m-%d'))})!=None):
                print("in add c loca-4")
                Mailer().send('18h61a05n3@cvsr.ac.in',name,location)
            payload={"message":"success","status":200}
            return payload
    except Exception:
        print("-------Something Went Wrong--------")




