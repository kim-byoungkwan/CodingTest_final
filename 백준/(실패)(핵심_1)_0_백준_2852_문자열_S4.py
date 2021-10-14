arr = [0]*3

team_1_win = 0

team_2_win = 0

dict = {}



T = int(input())

for _ in range(T):

    team, time = input().split()

    team = int(team)

    time = list(map(int,time.split(':')))

    time_real = time[0]*60 + time[1]


    dict[team] += [time_real]

    arr[team] += 1


    if arr[1] > arr[2]:



        team_1_win = dict[1] - dict[2]

    elif arr[1] < arr[2]:

        team_2_win = dict[2] - dict[1]

    else:

        team_draw = time


answer_1 = 48*60 - team_1_win

answer_2 = 48*60 - team_2_win

print("{}:{}".format(answer_1//60,answer_1 % 60))

print("{}:{}".format(answer_2//60,answer_2 % 60))



