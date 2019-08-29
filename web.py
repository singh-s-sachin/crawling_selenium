import crawl_movement
import json
location=["amsterdam", "bangalore", "bogota", "boston", "brisbane", "brussels", "cairo", "cincinnati","hyderabad", "johannesburg", "leeds", "london", "los_angeles", "manchester", "melbourne", "miami", "mumbai", "nairobi", "new_delhi", "orlando", "paris", "perth", "pittsburgh", "san_francisco", "santiago", "sao_paulo","seattle", "stockholm", "sydney", "taipei", "tampa", "toronto", "washington_DC" ,"west_midlands"]
prev1=open('initialize.json','r+')
d=open('yourjson.json','r+')
prev=json.loads(prev1.read())
place=prev["count"]
print(place)
n=len(location)
if(place==n):
    place=0
while(place<n):
    page = "https://movement.uber.com/explore/"+location[place]+"/?lang=en-US"
    crawl_movement.crwal(page,location[place])
    place+=1
    prev["count"]=place
    prev1.seek(0)
    json.dump(prev, prev1)
    prev1.truncate()
    d.seek(0)
    json.dump({}, d)
    d.truncate()
