###.1 (sparta_1w_##.3)

input = [3, 5, 6, 1, 2, 4]

def find_max_num(array):

    for num in array:

        for compare_num in array:

            if num < compare_num:

                break

        else:

            return num

# for - else 구문은 for문의 모든 요소값에 대한 반복동작이 일어났음에도 break에 의해 중단되지 않고 끝까지 실행되는 경우, 그 순간에 실행되는 동작을 else 문에 규정해주는 문법을 의미한다.

result = find_max_num(input)

print(result)
