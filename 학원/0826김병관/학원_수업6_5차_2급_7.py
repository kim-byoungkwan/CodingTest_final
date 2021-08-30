def solution(stuffs):

    box_small = []

    box_big = []

    for i in stuffs:

        if i <= 3:

            box_small.append(i)

        else:

            box_big.append(i)

    return max(sum(box_big),sum(box_small))

stuffs = [5,3,4,2,3,2]

print(solution(stuffs))