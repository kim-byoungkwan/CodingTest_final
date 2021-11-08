N = int(input())

dict = {}

for _ in range(N):

    nation, num, score = map(int, input().split())

    dict[(nation,num)] = dict.get((nation,num),0) + score

answer = []

count = 0

dict_new = {}

for key,value in sorted(dict.items(),key=lambda x : -x[1]):

    key = list(map(str,key))

    dict_new[key[0][0]] = dict_new.get(key[0][0],0) +1

    if dict_new[key[0][0]] >= 3:

        continue

    else:

        count +=1

        if count <4:

            answer.append(key)

        else:

            break

for value in answer:

    print(' '.join(value))
