###.04 최대값 찾기

##.1

# input = [3, 5, 6, 1, 2, 4]
#
# def find_max_num(array):
#
#     answer = max(array)
#
#     return answer
#
#
# result = find_max_num(input)
#
# print(result)

##.2

# input = [3, 5, 6, 1, 2, 4]
#
# def find_max_num(array):
#
#     answer = 0
#
#     for i in array:
#
#         if i > answer:
#
#             answer = i
#
#     return answer
#
# result = find_max_num(input)
#
# print(result)

##.3

# input = [3, 5, 6, 1, 2, 4]
#
# def find_max_num(array):
#
#     for num in array:
#
#         for compare_num in array:
#
#             if num < compare_num:
#
#                 break
#
#         else:
#
#             return num
#
# # for - else 구문은 for문의 모든 요소값에 대한 반복동작이 일어났음에도 break에 의해 중단되지 않고 끝까지 실행되는 경우, 그 순간에 실행되는 동작을 else 문에 규정해주는 문법을 의미한다.
#
# result = find_max_num(input)
#
# print(result)

##.conclusion

# 시간효율성은 ##.2 코드가 ##.3에 비해 for문이 한개만 쓰였으므로 더 좋다.





###.05 최빈값찾기

##.1

# input = "hello my name is sparta"
#
# def find_max_occurred_alphabet(string):
#
#     result = [0]*26
#
#     for i in string:
#
#         if i == ' ':
#
#             continue
#
#         else:
#
#             index = ord(i)-97
#
#             result[index] += 1
#
#     return chr(result.index(max(result))+97)
#
# answer = find_max_occurred_alphabet(input)
#
# print(answer)

##.2

# input = "hello my name is sparta"
#
# def find_max_occurred_alphabet(string):
#
#     result = [0]*26
#
#     for i in string:
#
#         if i.isalpha():
#
#             index = ord(i)-97
#
#             result[index] += 1
#
#     return chr(result.index(max(result))+97)
#
# result = find_max_occurred_alphabet(input)
#
# print(result)

# for문에서 continue는 다음요소값의 반복문으로 바로 넘어가라는 의미를 갖는다.

##.3

# def find_alphabet_occurrence_array(string):
#
#     alphabet_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k","l", "m", "n", "o", "p", "q", "r", "s","t", "u", "v","x", "y", "z"]
#
#     max_ouccurance = 0
#
#     max_alphabet = 0
#
#     for alphabet in alphabet_array:
#
#         ouccurance = 0
#
#         for str in string:
#
#             if alphabet == str:
#
#                 ouccurance +=1
#
#         if max_ouccurance < ouccurance:
#
#             max_ouccurance = ouccurance
#
#             max_alphabet = alphabet
#
#     return max_alphabet
#
# print(find_alphabet_occurrence_array("Hello my name is sparta"))




###.06 시간복잡도

# 시간복잡도는 입력값이 변화함에 따라 결정되는 코드의 출력 시간을 표현하는 개념으로, 입격값과 코드의 출력시간간의 함수를 의미하는 개념이다. 그러므로, 정의역의 변수를 입력값이라고 할때, 정의역의 변수 n에 대한 함수식으로 시간복잡도가 표현될 수 있는 것이다. ex logn , n*n 등등 이때 ,n은 입력값의 개수를 표현하는 정의역 변수이다.




###.07 공간복잡도

# 공간복잡도는 코드 전체를 하나의 사진으로 찍었을 때, 저장되어 있는 데이터의 개수를 의미한다고도 볼 수 있다.


###.08 점근 표기법

##.1

# input = [3, 5, 6, 1, 2, 4]
#
# def is_number_exist(number, array):
#
#     if number in array:
#
#         return True
#
#     else:
#
#         return False
#
# result = is_number_exist(3, input)
#
# print(result)


##.2

# input = [3, 5, 6, 1, 2, 4]
#
#
# def is_number_exist(number, array):
#
#     for element in array:
#
#         if element == number:
#
#             return True
#
#     return False
#
#
# result = is_number_exist(3, input)
#
# print(result)


###.09 알고리즘 더 풀어보기 (1)

# input = [0, 3, 5, 6, 1, 2, 4]
#
# def find_max_plus_or_multiply(array):
#
#     max = 0
#
#     for number in array:
#
#         if number <=1 or max <=1:
#
#             max += number
#
#         else:
#
#             max *= number
#
#     return max
#
# result = find_max_plus_or_multiply(input)
#
# print(result)



###.10 알고리즘 더 풀어보기 (2)

##.1

# input = "abacabade"
#
# def find_not_repeating_character(string):
#
#     dict = {}
#
#     answer = []
#
#     for i in string:
#
#         dict[i] = dict.get(i,0) + 1
#
#     for key,value in dict.items():
#
#         if value ==1:
#
#             answer.append(key)
#
#         else:
#
#             continue
#
#     if answer:
#
#         return answer[0]
#
#     else:
#
#         return '_'
#
# result = find_not_repeating_character(input)
#
# print(result)


##.2

input = "abacabade"


def find_not_repeating_character(string):

    result = [0]*150

    answer = []

    for i in string:

        index = ord(i)

        result[index] += 1

    for key,value in enumerate(result):

        if value == 1:

            answer.append(chr(key))

        else:

            continue

    for j in string:

        if j in answer:

            return j

    return '_'

result = find_not_repeating_character(input)

print(result)






