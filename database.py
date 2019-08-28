import pandas as pd
import json
import os
from pymongo import MongoClient
def show_data(file,file1,location):
    file=str("/home/sachin/Downloads/"+file)
    if(not os.path.exists(file)):
        file=str("/home/sachin/Downloads/"+file1)
    print(file)
    data = pd.read_csv(file) 
    data.to_json('yourjson.json')
    jdf = open('yourjson.json').read()
    df= json.loads(jdf)
    try:
        client = MongoClient("localhost",27017)
        db=client.uber
        oid=df["sourceid"]
        oid=[value for key,value in oid.items()]
        did=df["dstid"]
        did=[value for key,value in did.items()]
        mean=df["mean_travel_time"]
        mean=[value for key,value in mean.items()]
        standard=df["standard_deviation_travel_time"]
        standard=[value for key,value in standard.items()]
        geometric=df["geometric_mean_travel_time"]
        geometric=[value for key,value in geometric.items()]
        geometric_standard=df["geometric_standard_deviation_travel_time"]
        geometric_standard=[value for key,value in geometric_standard.items()]
        for i in range(len(oid)):
            post={"origin_id":oid[i],"destination_id":did[i],"mean_travel_time":mean[i],"standard_deviation_time":standard[i],"geometric_mean_time":geometric[i],"geometric_standard_mean_time":geometric_standard[i],"city":location}
            k=db.rides.insert(post)
            print(k)
        print("ALL DATA STORED IN LOCAL DATABASE")
    except Exception as e:
        print("Error connecting MongoClient", e)
