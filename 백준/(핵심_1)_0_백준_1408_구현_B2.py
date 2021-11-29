current = list(map(int,input().split(':')))

start = list(map(int,input().split(':')))

current[0] = current[0]*60*60

current[1] = current[1]*60

start[0] = start[0]*60*60

start[1] = start[1]*60


current_total = sum(current)

start_total = sum(start)

if current_total <= start_total:

    answer = start_total - current_total

else:

    answer = 24*60*60 - (current_total - start_total)

first = answer // (60*60)

first = str(first).zfill(2)

answer = answer % (60*60)

second = answer // 60

second = str(second).zfill(2)

third = answer % 60

third = str(third).zfill(2)

print('{}:{}:{}'.format(first,second,third))
