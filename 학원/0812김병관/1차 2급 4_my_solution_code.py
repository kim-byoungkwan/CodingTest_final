def func_a(arr):
    counter = [0,0,0,0,0,0,0,0,0,0]
    for x in arr:
        counter[x] =counter[x] + 1
    return counter

def func_b(arr):
    ret = 0
    for x in arr:
        if ret < x:
            ret = x
    return ret

def func_c(arr):
    ret = 10
    for x in arr:
        if x != 0 and ret > x:
            ret = x
    return ret

def solution(arr):
    counter = func_a(arr)
    max_cnt = func_b(counter)
    min_cnt = func_c(counter)
    return max_cnt // min_cnt


arr = [1, 2, 3, 3, 1, 3, 3, 2, 3, 2]
ret = solution(arr)

print(ret)
