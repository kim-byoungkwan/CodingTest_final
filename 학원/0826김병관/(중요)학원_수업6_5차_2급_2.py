###.1

from collections import deque

time_table = [0,1,0,1,0,0,1,0,1,0,0,0,1,0,0]

def solution(time_table):

    queue = deque(time_table)

    while queue[-1] == 0:

        queue.pop()

    while queue[0] == 0:

        queue.popleft()

    answer = queue.count(0)

    return answer

print(solution(time_table))

###.sol

def func_a(time_table):

    answer = 0

    for i, t in reversed(list(enumerate(time_table))):

        #print(i,t)

        if t == 1:

            answer = i

            break

    return answer

def func_b(time_table,class1,class2):

    answer = 0

    for i in range(class1,class2):

        if time_table[i] == 0:

            answer += 1

    return answer

def func_c(time_table):

    answer = 0

    for i, t in enumerate(time_table):

        if t == 1:

            answer = i

            break

    return answer

def solution(time_table):

    answer = 0

    first_class = func_c(time_table)

    last_class = func_a(time_table)

    answer = func_b(time_table,first_class,last_class)

    return answer


time_table = [1,1,0,0,1,0,1,0,0,0]

ret = solution(time_table)

print(ret)

