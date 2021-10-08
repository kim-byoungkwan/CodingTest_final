S = input()

result = []

for i in range(len(S)-2):

    for j in range(i+1,len(S)-1):

        for k in range(j+1,len(S)):

            result.append(S[:j][::-1] + S[j:k][::-1] + S[k:][::-1])

print(sorted(result)[0])
