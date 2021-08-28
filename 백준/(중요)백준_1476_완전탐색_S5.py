from collections import deque

import copy

E,S,M = map(int,input().split())

count = 0


E_queue = deque()

S_queue = deque()

M_queue = deque()


for i in range(1, 16):

    E_queue.append(i)

for j in range(1, 29):

    S_queue.append(j)

for m in range(1, 20):

    M_queue.append(m)


E_copy = copy.deepcopy(E_queue)

S_copy = copy.deepcopy(S_queue)

M_copy = copy.deepcopy(M_queue)


while True:

    temp_E = E_queue.popleft()

    temp_S = S_queue.popleft()

    temp_M = M_queue.popleft()

    count = count + 1

    if len(E_queue) == 0:

        E_queue = copy.deepcopy(E_copy)

    if len(S_queue) == 0:

        S_queue = copy.deepcopy(S_copy)

    if len(M_queue) == 0:

        M_queue = copy.deepcopy(M_copy)

    if temp_E == E and temp_S == S and temp_M == M:

        print(count)

        break

    else:

        continue


