import os
os.system('ls')
if not os.path.exists("/home/sachin/Downloads/Uber"):
    os.chdir("/home/sachin/Downloads")
    os.system("mkdir Uber")
city=input("Enter location")
try:
    command="mongoexport --db uber --collection "+city+" --fields _id,origin_id,destination_id,mean_travel_time,standard_deviation_time,geometric_mean_time,geometric_standard_mean_time --type=csv --out /home/sachin/Downloads/Uber/Travel_time_"+city+".csv"
    os.system(command)
except:
    print("Connect to MongoClient/Database dosent exists")