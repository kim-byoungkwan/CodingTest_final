from collections import deque

N = int(input())

answer = list(input())

dict = {'Adrian':0,
        'Bruno':0,
        'Goran':0}

Adrian = deque(['A','B','C'])

Bruno = deque(['B','A','B','C'])

Goran = deque(['C','C','A','A','B','B'])


for i in range(N):

    Adrian_out = Adrian.popleft()

    Adrian.append(Adrian_out)


    Bruno_out = Bruno.popleft()

    Bruno.append(Bruno_out)


    Goran_out = Goran.popleft()

    Goran.append(Goran_out)


    if answer[i] == Adrian_out:

        dict['Adrian'] = dict.get('Adrian',0) + 1

    if answer[i] == Bruno_out:

        dict['Bruno'] = dict.get('Bruno',0) + 1

    if answer[i] == Goran_out:

        dict['Goran'] = dict.get('Goran',0) + 1

max_value = max(list(dict.values()))

box = []

for key,value in dict.items():

    if value == max_value:

       box.append(key)

print(max_value)

for j in box:

    print(j)
