N_list = list(input())

former_arr = []

latter_arr = []

count = 0

for i in N_list:

    count += 1

    if count <= len(N_list)//2:

        former_arr.append(int(i))

    else:

        latter_arr.append(int(i))

if sum(former_arr) == sum(latter_arr):

    print("LUCKY")

else:

    print("READY")

