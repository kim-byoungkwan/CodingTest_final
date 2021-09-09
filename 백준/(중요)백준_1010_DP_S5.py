###.1

# from itertools import combinations
#
# T = int(input())
#
# N,M = map(int,input().split())
#
# list_all = [i for i in range(1,M+1)]
#
# output = list(combinations(list_all,N))
#
# print(len(output))


###.2

def factorial(n):

    if n <= 1:

        return 1

    else:

        return n*factorial(n-1)

T = int(input())

for _ in range(T):

    N,M = map(int,input().split())

    result = int((factorial(M) / (factorial(M-N) * factorial(N))))

    print(result)

