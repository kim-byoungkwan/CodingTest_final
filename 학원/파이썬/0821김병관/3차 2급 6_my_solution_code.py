def solution(length):
    answer = ''
    com = 'RRRGGB'
    if length%6 ==1 or length%6 ==2 or length%6 ==4:
        answer = '-1'
    else:
        for i in range(length):
            answer+=com[i % 6]
    return answer


tile_length1 = 11
ret1 = solution(tile_length1)
print(ret1)

tile_length2 = 16
ret2 = solution(tile_length2)
print(ret2)
