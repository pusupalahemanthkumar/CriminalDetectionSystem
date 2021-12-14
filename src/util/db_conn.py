import pymongo
from util.config import get_mongodb_url

def connect_db():
    client = pymongo.MongoClient(get_mongodb_url(), ssl=True,ssl_cert_reqs='CERT_NONE')
    try:
        print(client.server_info())
        print()
        print("-------------------Connected-------------------")
    except Exception:
        print(Exception)
        print("Unable to connect to the server.")
        return None
        
    return client["CriminalDetectionSystem"]
