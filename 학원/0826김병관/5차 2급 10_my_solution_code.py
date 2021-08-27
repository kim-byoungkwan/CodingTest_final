def solution(time_table, n):
    answer = 0
    lst = [0 for _ in range(n)]
    for i, t in enumerate(time_table):
    	lst[i % n] += t
    answer = max(lst)
    return answer


time_table1 = [1, 5, 1, 9]
n1 = 3
ret1 = solution(time_table1, n1)
print(ret1)

time_table2 = [4, 8, 2, 5, 4, 6, 7]
n2 = 4
ret2 = solution(time_table2, n2)
print(ret2)
