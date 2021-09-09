def solution(papers,K):
    length = len(papers)
    for i, paper in enumerate(papers):
        K -= paper
        if K < 0:
            return i
    return length


papers1 = [2,4,2,3,1]
K1 = 10
ret1 = solution(papers1,K1)
print(ret1)

papers2 = [2,4,2,3,1]
K2 = 14
ret2 = solution(papers2,K2)
print(ret2)
