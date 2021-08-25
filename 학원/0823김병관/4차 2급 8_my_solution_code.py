def solution(n, votes):
    arr = [0] * (n + 1)
    max_value = 0
    for vote in votes:
        arr[vote] += 1
        if arr[vote] > max_value:
            max_value = arr[vote]
            a_vote = vote
            
    if max_value >= len(votes)/2:
        return a_vote
    else:
        return -1


n1 = 3
votes1 = [1,2,1,3,1,2,1]
ret1 = solution(n1, votes1)
print(ret1)


n2 = 2
votes2 = [2,1,2,1,2,2,1]
ret2 = solution(n2, votes2)
print(ret2)
