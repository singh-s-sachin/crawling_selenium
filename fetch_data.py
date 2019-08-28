import csv
import json
import os
from os import path
import shutil
from pymongo import MongoClient
def putdata(location):
    file_name="traveltime_"+location+".csv"
    src=path.realpath(file_name)
    print(src)
    shutil.copy(src,"/home/sachin/Downloads")
def get_data(loc):
    file_name="traveltime_"+loc+".csv"
    try:
        client = MongoClient("localhost",27017)
        db=client.uber
        data=db[loc].find()
        print(data.count(),"datas")
        lst=[]
        print("Processing....\nPlease wait for few seconds")
        l=[["SNo.","Origin id","Destination id","Mean time","Standard deviation Time","Geometric mean time","Standard geometric mean time"]]
        with open(file_name, 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(l)
            print("Exporting your request. Have patience.")
            print("This may take upto several minutes.")
            for i in range(data.count()):
                temp=data[i]
                l=[i+1,temp["origin_id"],temp["destination_id"],temp["mean_travel_time"],temp["standard_deviation_time"],temp["geometric_mean_time"],temp["geometric_standard_mean_time"]]
                lst.append(l)
                if i%1234==0:
                    print(i,"/",data.count())
            print("Writing your data")
            writer.writerows(lst)
            print(i,"/",data.count())
            putdata(loc)
            print("Data saved in your download folder : ",file_name)
        writeFile.close()
    except:
        print("Something went wrong")
loc=input()
get_data(loc)