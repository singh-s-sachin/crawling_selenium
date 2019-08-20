import pandas as pd
import json
from pymongo import MongoClient
def show_data():
    data = pd.read_csv("/home/sachin/Downloads/Travel_Times.csv") 
    data.to_json('yourjson.json')
    jdf = open('yourjson.json').read()
    df= json.loads(jdf)
    try:
        client = MongoClient("localhost",27017)
        db=client.uber
        oid=df["Origin Movement ID"]
        oid=[value for key,value in oid.items()]
        o=df["Origin Display Name"]
        o=[value for key,value in o.items()]
        did=df["Destination Movement ID"]
        did=[value for key,value in did.items()]
        d=df["Destination Display Name"]
        d=[value for key,value in d.items()]
        mean=df["Mean Travel Time (Seconds)"]
        mean=[value for key,value in mean.items()]
        upper=df["Range - Lower Bound Travel Time (Seconds)"]
        upper=[value for key,value in upper.items()]
        lower=df["Range - Upper Bound Travel Time (Seconds)"]
        lower=[value for key,value in lower.items()]
        date=df["Date Range"]
        date=[value for key,value in date.items()]
        for i in range(len(o)):
            post={"origin_id":oid[i],"origin":o[i],"destination_id":did[i],"destination":d[i],"mean_travel_time":mean[i],"max_time":upper[i],"min_time":lower[i],"date_range":date}
            k=db.rides.insert(post)
            print(k)
        print("ALL DATA STORED IN LOCAL DATABASE")
    except Exception as e:
        print("Error connecting MongoClient", e)
