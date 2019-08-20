import csv
import json
import os
from os import path
import shutil
from pymongo import MongoClient
def putdata():
    src=path.realpath("traveltime.csv")
    print(src)
    shutil.copy(src,"/home/sachin/Downloads")
def get_data():
    try:
        client = MongoClient("localhost",27017)
        db=client.uber
        data=db.rides.find()
        print(data.count(),"datas")
        print("Processing....\nPlease wait for few seconds")
        l=[["SNo.","Origin id","Origin","Destination id","Destination","Max time","Min Time","Mean time","Date Range"]]
        with open('traveltime.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(l)
            lst=[]
            for i in range(data.count()):
                temp=data[i]
                l=[i+1,temp["origin_id"],temp["origin"],temp["destination_id"],temp["destination"],temp["max_time"],temp["min_time"],temp["mean_travel_time"],temp["date_range"]]
                lst.append(l)
                if(i%234==0 and i>5000):
                    print(i,"/",data.count())
            writer.writerows(lst)
            print(i,"/",data.count())
            putdata()
            print("Data saved in your download folder : traveltime.csv")
        writeFile.close()
    except:
        print("Something went wrong")
get_data()