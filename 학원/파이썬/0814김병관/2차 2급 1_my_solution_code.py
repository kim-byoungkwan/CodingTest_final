def func_a(arr):
    counter = [0,0,0,0,0,0,0,0,0,0,0]
    for x in arr:
        counter[x] += 1
    return counter

def solution(left_gloves,right_gloves):
    left_counter = func_a(left_gloves)
    right_counter = func_a(right_gloves)
    
    total = 0
    for i in range(1,11):
        total += min(left_counter[i],right_counter[i])
    return total


left_gloves = [2,1,2,2,4]
right_gloves = [1,2,2,4,4,7]
ret = solution(left_gloves,right_gloves)

print(ret)
