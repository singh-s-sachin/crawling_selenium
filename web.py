import crawl_movement
import json
page = "https://movement.uber.com/explore/bangalore/travel-times/query?lang=hi-IN&si=89&ti=94&ag=wards&sa;=&ta;=&dt[tpb]=ALL_DAY&dt[wd;]=1,2,3,4,5,6,7&dt[dr][sd]=2018-12-01&dt[dr][ed]=2018-12-31&cd=&lat.=12.9410403&lng.=77.585093&z.=10.79&sdn=&tdn="
prev1=open('initialize.json','r+')
d=open('yourjson.json','r+')
prev=json.loads(prev1.read())
place=prev["count"]
print(place)
if(place==19):
	place+=1
if(place==35):
    place=0
while(place<35):
    crawl_movement.crwal(page,place)
    place+=1
    prev["count"]=place
    prev1.seek(0)
    json.dump(prev, prev1)
    prev1.truncate()
    d.seek(0)
    json.dump({}, d)
    d.truncate()
