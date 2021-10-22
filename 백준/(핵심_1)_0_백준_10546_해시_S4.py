import sys

N = int(sys.stdin.readline())

dict = {}

for _ in range(N):

    all_participant = sys.stdin.readline()

    dict[all_participant] = dict.get(all_participant,0) +1

for _ in range(N-1):

    finish = sys.stdin.readline()

    dict[finish] = dict.get(finish,0) -1

print(sorted(dict.items(),key= lambda x: -x[1])[0][0])
