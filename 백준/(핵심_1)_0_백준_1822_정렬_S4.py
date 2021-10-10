N_A,N_B = map(int,input().split())

set_A = set(map(int,input().split()))

set_B = set(map(int,input().split()))

answer = set_A - set_B

print(len(answer))

print(*sorted(answer))