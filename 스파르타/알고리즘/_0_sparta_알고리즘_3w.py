###.01 정렬_1

##.ex1

# input = [4, 6, 2, 9, 1]
#
# def bubble_sort(array):
#
#     for k in range(len(array)):
#
#         for i in range(1,len(array)-k):
#
#             if array[i-1] > array[i]:
#
#                 array[i-1],array[i] = array[i],array[i-1]
#
#     return array
#
# bubble_sort(input)
#
# print(input)

# O(N^2)


###.02 정렬_2

##.ex1

# input = [4, 6, 2, 9, 1]
#
# def selection_sort(array):
#
#     for k in range(len(array)):
#
#         for i in range(k,len(array)):
#
#             if array[k] > array[i]:
#
#                 array[k],array[i] = array[i],array[k]
#
#     return array
#
# print(selection_sort(input))

# O(N^2)


##.ex3

# input = [4, 6, 2, 9, 1]
#
# def insertion_sort(array):
#
#     for i in range(1,len(array)):
#
#         for j in range(i):
#
#             if array[i-j-1] > array[i-j]:
#
#                 array[i-j-1],array[i-j] = array[i-j],array[i-j-1]
#
#             else:
#
#                 break
#
#     return array
#
# insertion_sort(input)
#
# print(input)

# [1,2,3,4,5]의 배열이 주어질 경우 위의 삽입정렬은 O(N^2)의 일반적인 상황의 시간복잡도에서 O(N)의 시간복잡도로 축소되는 효율성이 발생하게된다.


###.03 정렬_3

##.ex1

# def merge(array1, array2):
#
#     array_c = []
#
#     array1_index = 0
#
#     array2_index = 0
#
#     while array1_index < len(array1) and array2_index < len(array2):
#
#         if array1[array1_index] < array2[array2_index]:
#
#             array_c.append(array1[array1_index])
#
#             array1_index +=1
#
#         else:
#
#             array_c.append(array2[array2_index])
#
#             array2_index +=1
#
#     if array1_index == len(array1):
#
#         while array2_index < len(array2):
#
#             array_c.append(array2[array2_index])
#
#             array2_index +=1
#
#     if array2_index == len(array2):
#
#         while array1_index < len(array1):
#
#             array_c.append(array1[array1_index])
#
#             array1_index +=1
#
#     return array_c

# merge 함수는 array1,array2의 크기가 2/N이므로, 최대 O(N)의 시간복잡도를 갖는다.

##.ex2

# array = [5, 3, 2, 1, 6, 8, 7, 4]
#
# def merge_sort(array):
#
#     if len(array) <=1:
#
#         return array
#
#     mid = (0 + len(array)) //2
#
#     left_array = merge_sort(array[:mid])
#
#     right_array = merge_sort(array[mid:])
#
#     return merge(left_array,right_array)
#
# print(merge_sort(array))

# merge_sort 함수의 시간복잡도는 O(N)의 시간복잡도의 merge 함수를 이 경우 N = 8 = 2^3이므로 3단계의 merge가 발생하게 되는데 임의의 k단계에 대하여 N = 2^k이므로 k는 2를 밑으로하는 N의 로그값이므로 k = log2N으로 표현할 수있고,
# 이를 간략화하면, k = logN이므로 임의의 k단계마다 logN의 시간복잡도가 발생한다는 것이다. 즉, k단계라고 했을 때 총 발생하는 시간복잡도는 O(NlogN)으로 결정된다.


###.04 스택

# class Node:
#
#     def __init__(self, data):
#
#         self.data = data
#
#         self.next = None
#
#
# class Stack:
#
#     def __init__(self):
#
#         self.head = None
#
#     def push(self, value):
#
#         new_head = Node(value)
#
#         new_head.next = self.head
#
#         self.head = new_head
#
#     def pop(self):
#
#         if self.is_empty():
#
#             return "Stack is Empty"
#
#         delete_head = self.head
#
#         self.head = self.head.next
#
#         return delete_head.data
#
#     def peek(self):
#
#         if self.is_empty():
#
# # self는 peek 메소드가 속한 클래스를 의히하고, 또한 이 클래스로 부터 생성될 클래스의 모든 속성을 갖는 미래에 존재할 객체 그 자체를 의미한다. 그래서 미래에 peek를 적용할 어떠한 객체 그 자체가 비어있음의 여부를 self.is_empty()로 표현할 수 있다.
#
#             return "Stack is empty"
#
#         return self.head.data
#
#     def is_empty(self):
#
#         return self.head is None

#
# stack = Stack()
#
# stack.push(3)
#
# print(stack.peek())
#
# stack.push(4)
#
# print(stack.peek())
#
# print(stack.pop())
#
# print(stack.peek())
#
# print(stack.is_empty())


##.ex1

# top_heights = [10, 9, 5, 7, 4]
#
#
# def get_receiver_top_orders(heights):
#
#     answer = [0] * len(heights)
#
#     while heights:
#
#         height = heights.pop()
#
#         for idx in range(len(heights)-1,-1,-1):
#
#             if heights[idx] > height:
#
#                 answer[len(heights)] = idx+1
#
#                 break
#
#     return answer
#
# print(get_receiver_top_orders(top_heights))

# O(N^2)

###.05 큐

# class Node:
#     def __init__(self, data):
#
#         self.data = data
#
#         self.next = None
#
# class Queue:
#
#     def __init__(self):
#
#         self.head = None
#
#         self.tail = None
#
#     def enqueue(self, value):
#
#         new_node = Node(value)
#
#         if self.is_empty():
#
#             self.head = new_node
#
#             self.tail = new_node
#
#             return
#
#         self.tail.next = new_node
#
#         self.tail = new_node
#
#     def dequeue(self):
#
#         if self.is_empty():
#
#             return "Queue is Empty"
#
#         delete_node = self.head
#
#         self.head = self.head.next
#
#         return delete_node.data
#
#     def peek(self):
#
#         if self.is_empty():
#
#             return "Queue is Empty"
#
#         return self.head.data
#
#     def is_empty(self):
#
#         return self.head is None

# queue = Queue()
#
# queue.enqueue(3)
#
# print(queue.peek())
#
# queue.enqueue(4)
#
# print(queue.peek())
#
# queue.enqueue(5)
#
# print(queue.peek())
#
# queue.dequeue()
#
# print(queue.peek())
#
# print(queue.is_empty())
#
# print(queue.dequeue())


###.06 해쉬_1


# items = [None] * 8
#
# items[hash("fast") % 8] = "빠른"
#
# items[hash("slow") % 8] = "느린"

# 8로 나누었을 때 발생할 수 있는 값은 0,1,2 ~ 7 이므로 8개의 인덱스를 가진 배열의 모든 인덱스를 표현할 수 있게된다.

# 위의 배열의 인덱스를 이용해 값을 할당하는 동작은 O(1)만큼의 시간복잡도를 갖는다.

# print(items)
#
# print(items[hash("fast") % 8])


# class Dict:
#
#     def __init__(self):
#
#         self.items = [None] * 8
#
#     def put(self,key,value):
#
#         index = hash(key) % len(self.items)
#
#         self.items[index] = value
#
#         return
#
#     def get(self,key):
#
#         index = hash(key) % len(self.items)
#
#         return self.items[index]
#
#
# my_dict = Dict()
#
# my_dict.put("test",3)
#
# print(my_dict.get("test"))
#
#
# class LinkedTuple:
#
#     def __init__(self):
#
#         self.items = list()
#
#     def add(self,key,value):
#
#         self.items.append((key,value))
#
#     def get(self,key):
#
#         for k,v in self.items:
#
#             if key == k:
#
#                 return v
#
# class LinkedDict:
#
#     def __init__(self):
#
#         self.items = []
#
#         for i in range(8):
#
#             self.items.append(LinkedTuple())
#
#
#     def put(self,key,value):
#
#         index = hash(key) % len(self.items)
#
# # 주어진 key에 대한 index를 정의해준다.
#
#         self.items[index].add((key,value))
#
# # 이때의 items에는 LinkedTuple 클래스의 객체가 존재한다. 이때 이 객체는 add 메소드를 적용할 수 있으므로 add 메소드를 적용하여 리스트 자료형태의 객체에 값을 추가해준다.
#
#         return
#
#     def get(self,key):
#
#         index = hash(key) % len(self.items)
#
#         return self.items[index].get(key)
#
# # 이때 items[index]가 표현하는 것은 LinkedTuple 클래스로 부터 생성된 객체고, 이 객체는 리스트 자료형으로 get 메소드를 적용하여 value를 구할 수 있으므로 위와같이 표현한다.
#
# # 위와같이 key와 value를 이용하면 동일한 value의 값을 저장하더라도 값의 손실 없이 모두 저장할 수 있게된다.



###.07 해쉬_2

##.ex1

# all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
# present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]
#
#
# def get_absent_student(all_array, present_array):
#
#     dict = {}
#
#     for all in all_array: # O(N)
#
#         dict[all] = dict.get(all,0) +1 # 공간복잡도 O(N)
#
#     for present in present_array: # O(N)
#
#         dict[present] = dict.get(present,0) -1
#
#     return sorted(dict.items(),key= lambda x: -x[1])[0][0]
#
# print(get_absent_student(all_students, present_students))

# O(N)


###.08 숙제

##.ex1

# shop_prices = [30000, 2000, 1500000]
#
# user_coupons = [20, 40]
#
# def get_max_discounted_price(prices, coupons):
#
#     prices.sort(reverse=True)
#
#     coupons.sort(reverse=True)
#
#     prices_index = 0
#
#     coupons_index = 0
#
#     cost = 0
#
#     while prices_index < len(prices) and coupons_index < len(coupons):
#
#         cost += prices[prices_index] * ((100-coupons[coupons_index]) /100)
#
#         prices_index +=1
#
#         coupons_index +=1
#
#     while prices_index < len(prices):
#
#         cost += prices[prices_index]
#
#         prices_index +=1
#
#     return cost
#
# print(int(get_max_discounted_price(shop_prices, user_coupons)))
#


##.ex2

# s = "(((("
#
# def is_correct_parenthesis(string):
#
#     stack = []
#
#     for i in string:
#
#         if i == '(':
#
#             stack.append(i)
#
#         else:
#
#             if stack:
#
#                 if stack[-1] == '(':
#
#                     stack.pop()
#
#                 else:
#
#                     return False
#
#             else:
#
#                 return False
#
#     if stack:
#
#         return False
#
#     else:
#
#         return True
#
# print(is_correct_parenthesis(s))
#


##.ex3

# genres = ["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"]
#
# plays = [2000, 500, 600, 150, 800, 2500, 2000]
#
#
# def get_melon_best_album(genres, plays):
#
#     answer = []
#
#     dict_genre_count = {}
#
#     for idx in range(len(genres)):
#
#         dict_genre_count[genres[idx]] = dict_genre_count.get(genres[idx],0) + plays[idx]
#
#     dict_genre_count = sorted(dict_genre_count.items(), key=lambda item: -item[1])
#
#
#
#     dict_genre_in_count = {}
#
#     for idx in range(len(genres)):
#
#         dict_genre_in_count[genres[idx]] = dict_genre_in_count.get(genres[idx],[]) + [(idx,plays[idx])]
#
#
#     for key,value in dict_genre_in_count.items():
#
#         value = sorted(value,key=lambda x:(-x[1],x[0]))
#
#         dict_genre_in_count[key] = value
#
#
#     for key,value in dict_genre_count:
#
#         count = 0
#
#         for result in dict_genre_in_count[key]:
#
#             count +=1
#
#             if count <=2:
#
#                 answer.append(result[0])
#
#     return answer
#
# print(get_melon_best_album(genres, plays))















