from datetime import datetime

parse_now = list(map(int,input().split(':')))

now = datetime(1,1,1,parse_now[0],parse_now[1],parse_now[2])

parse_future = list(map(int,input().split(':')))

future = datetime(1,1,1,parse_future[0],parse_future[1],parse_future[2])


if future < now:

    print(now - future)

else:

    print(future-now)







