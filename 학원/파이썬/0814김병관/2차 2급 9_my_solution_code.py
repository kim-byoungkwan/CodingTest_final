def solution(votes,N,K):
    counter = [0,0,0,0,0,0]
    for x in votes:
        counter[x] += 1
    answer = 0
    for c in counter:
        if c == K:
            answer += 1
    return answer


votes = [2,5,3,4,1,5,1,5,5,3]
N = 5
K = 2
ret = solution(votes,N,K)
print(ret)
