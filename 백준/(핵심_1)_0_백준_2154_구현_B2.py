N = int(input())

result = ''

N_str = str(N)

for i in range(1,N+1):

    result += str(i)

print(result.index(N_str)+1)
