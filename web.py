import crawl_movement
page = "https://movement.uber.com/explore/bangalore/travel-times/query?lang=hi-IN&si=89&ti=94&ag=wards&sa;=&ta;=&dt[tpb]=ALL_DAY&dt[wd;]=1,2,3,4,5,6,7&dt[dr][sd]=2018-12-01&dt[dr][ed]=2018-12-31&cd=&lat.=12.9410403&lng.=77.585093&z.=10.79&sdn=&tdn="
place=1
while(place<35):
    crawl_movement.crwal(page,place)
    place+=1
