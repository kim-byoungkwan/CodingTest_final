###.1

import sys

T = int(sys.stdin.readline())

for _ in range(T):

    a, b = map(int, sys.stdin.readline().split())

    total = a ** b

    index = total % 10

    print(index)


###.2


