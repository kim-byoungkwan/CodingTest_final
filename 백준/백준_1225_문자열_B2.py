###.1

import sys

A,B = sys.stdin.readline().split()

A= list(map(int,A))

B= list(map(int,B))

answer = 0

for i in A:

    for j in B:

        answer = answer + i*j

print(answer)

###.2

import sys

A,B = sys.stdin.readline().split()

A= list(map(int,A))

B= list(map(int,B))

print(sum(A)*sum(B))