###.03 클래스

##.ex1

# class Person:
#
#     # pass
#
#     def __init__(self):
#
#         print("I am created", self)
#
# # class의 인자로 self가 지정될 때 이는 class로 인해 생성되는 객체 그 자체를 의미한다. 클래스를 정의하는 순간에는 아직 존재하지 않지만, 지금 정의하는 클래스로부터 미래에 생성될 객체 그 자체를 의미하는 것이 self이다.
#
#
# person_1 = Person()
#
# # 생성자는 클래스가 표현되는 그 순간 동시에 동작하여 표현되게된다.
#
# print(person_1)
#
# person_2 = Person()
#
# print(person_2)
#
# # 클래스 뒤에 사용되는 괄호 ()는 생성자를 호출하는 메소드를 의미한다.

##.ex2

# class Person:
#
#     def __init__(self, param_name):
#
# # 생성자가 동작할 때, 생성자에 의해 미래에 생성될 객체인 self에 param_name라는 변수에 인자를 받겠다는 의미이다.
#
# # 본질적인 의미는 init 이라는 생성자 메소드는 이 생성자에 의해 미래에 생성될 객체 self와, 이 생성자가 미래에 할당받게 될 변수 값 param_name에 의해 결정되는 메소드인데, 이 메소드는 이 생성자 메소드에 의해 생성될 미래의 객체 self에 변수 name를 정의하고 그 변수에 입력받은 param_name의 값을 할당하겠다는 의미이다.
#
#         print("I am created", self)
#
#         self.name = param_name
#
# # 생성자 내부에 name이라는 변수를 정의하고 그 변수에 param_name에 입력받은 값을 할당한다는 의미이다.
#
# person_1 = Person("유재석")
#
# print(person_1)
#
# person_2 = Person("박명수")
#
# print(person_2)
#
# "유재석", "박명수" 라는 문자를 생성자의 인수로 입력 받았지만, 생성자에의해 생성된 객체만 표현될 뿐 입력받은 문자열 "유재석","박명수"는 표현되지 않는다.


##.ex03

# class Person:
#
#     def __init__(self, param_name):
#
#         self.name = param_name
#
#         print("I am created", self.name)
#
#
# person_1 = Person("유재석")
#
# print(person_1)
#
# print(person_1.name)
#
# print('---------')
#
# person_2 = Person("박명수")
#
# print(person_2)
#
# print(person_2.name)


##.ex04

# class Person:
#
#     def __init__(self, param_name):
#
#         self.name = param_name
#
#         print("I am created", self.name)
#
#     def talk(self):
#
# # 클래스를 정의할 때, 클래스 내부의 메소드는 언젠가 미래에 지금 정의하는 클래스로부터 생성될 객체에 사용될 것이므로, 메소드를 정의하는 순간 자동으로 self가 인자로 표현되게 된다. 즉, 클래스에 정의된 메소드는 미래에 정의될 어떠한 객체에 반드시 사용될 메소드이므로 무조건 self가 클래스 내부의 메소도의 인자로 표현되게된다.
#
#         print("안녕하세요, 제 이름은",self.name,"입니다.")
#
#
# person_1 = Person("유재석")
#
# print(person_1)
#
# print(person_1.name)
#
# person_1.talk()
#
#
# print()
#
# print('-------------------------------------------------------------')
#
# print()
#
#
# person_2 = Person("박명수")
#
# print(person_2)
#
# print(person_2.name)
#
# person_2.talk()


###.04 링크드리스트 구현_1

# class Node:
#
#     def __init__(self,data):
#
#         self.data = data
#
#         self.next = None
#
#
# # node = Node(3)
# #
# # print(node)
#
# # node라는 변수는 생성자를 가진 Node라는 클래스에 3을 할당하여 형성되는 객체이다. 즉, node객체는 data라는 변수에 3을 갖고있고, next라는 변수에 None를 갖고 있는 객체이다.
#
# # '<__main__.Node object at 0x0000021C1D4E7400>' 실행결과 이와같이 출력되는데 이는 Node라는 클래스로부터 만들어진 객체 object가 0x0000021C1D4E7400 라는 주소를 가진 공간에 저장되어 있다는 것을 의미한다.
#
# # first_node = Node(4)
# #
# # node.next = first_node
# #
# # print(node.next.data)
#
# # node.next는 결국 어떠한 데이터를 저장할 수 있는 변수이고 현제 그 변수에 객체 first_node가 할당되어있다. 즉, node.next 자체가 본질적으로 이경우 first_node라는 객체인 것이다. 그러므로, node.next는 객체이므로 데이타를 저장하고 있는 data 변수가 존재하므로 node.next로부터 data를 node.next.data와 같이 불러들일 수 있다. 그 결과는 first_node 객체의 데이터인 4가 출력되게된다.
#
#
# # second_node = Node(12)
# #
# # first_node.next = second_node
# #
# # print(first_node.next.data)
#
# # first_node는 Node 클래스로부터 만들어진 객체이므로, 객체안에 데이터를 저장할 수 있는 data변수와 next 변수가 존재한다. 그러므로, next 변수에 어떠한 데이터를 할당할 수 있고, next 변수는 노드가 가리키는 다음 노드를 저장하는 저장공간 이므로 다음 노드를 second_node로 지정할 수 있다.
#
#
# class LinkedList:
#
#     def __init__(self,data):
#
#         self.head = Node(data)
#
#     def append(self,data):
#
#         if self.head is None:
#
#             self.head = Node(data)
#
#             return
#
# # None이라는 객체에는 다음 노드를 가리키는 next라는 객체가 존재할 수 없다. 그러므로, 연결리스트의 append가 성립하기 위해서 None에 어떠한 노드를 정의해줘야한다.
#
#         current = self.head
#
#         while current.next is not None:
#
#             current = current.next
#
#         current.next = Node(data)
#
# # 연결리스트의 마지막 노드에 추가하고자하는 데이터를 가진 노드를 붙여준다.
#
# # 위의 append의 논리는 current를 점점 다음 노드로 정의해가면서 끝의 노드가 될때까지 current를 끝의 노드로 옮겨주는 것이다.
#
#     def print_all(self):
#
#         current = self.head
#
#         while current is not None:
#
#             print(current.data)
#
#             current = current.next
#
#
# linked_list = LinkedList(3)
#
# print(linked_list)
#
# print(linked_list.head)
#
# print(linked_list.head.data)
#
# print(linked_list.head.next)
#
#
# linked_list.append(4)
#
# linked_list.append(5)
#
# linked_list.print_all()
#
#
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

###.05 링크드리스트_2

# class Node:
#
#     def __init__(self,data):
#
#         self.data = data
#
#         self.next = None
#
#
# class LinkedList:
#
#     def __init__(self, value):
#
#         self.head = Node(value)
#
#     def append(self, value):
#
#         cur = self.head
#
#         while cur.next is not None:
#
#             cur = cur.next
#
#         cur.next = Node(value)
#
#     def print_all(self):
#
#         cur = self.head
#
#         while cur is not None:
#
#             print(cur.data)
#
#             cur = cur.next
#
#     def get_node(self, index):
#
#         node = self.head
#
#         count = 0
#
#         while count < index:
#
#             node = node.next
#
#             count +=1
#
#         return node
#
#     def add_node(self, index, value):
#
#         new_node = Node(value)
#
#         if index == 0:
#
#             new_node.next = self.head
#
# # 기존에 head노드에 들어있던 노드값을 new_node의 다음노드로 정의해준다. 그리고
#
#             self.head = new_node
#
# # 현재의 head 노드를 내가 넣고자하는 new_node로 덮어씌어주면 기존의 head 노드에 저장되어있던 노드값도 보존하고 내가 넣고자하는 새로운 노드를 head에 넣을 수 있게된다.
#
#             return
#
#         node = self.get_node(index-1)
#
#         next_node = node.next
#
#         node.next = new_node
#
#         new_node.next = next_node
#
# # self는 class에 의해 만들어질 객체 그자체를 의미한다고 말했다. 이 의미는 class에 의해 만들어질 객체 그자체가 class그자체를 의미한다고 볼 수 있으므로, self는 본질적으로 class 그 자체를 의미한다고 볼 수 있다.
# # 그러므로, 같은 class 내부의 메소드를 다른 메소드에서 사용하기 위해선 클래스 자기 자신으로부터 메소드를 가져와야 하므로 self 라는 class 자기 자신을 의미하는 객체로부터 가져와야한다.
#
#     def delete_node(self,index):
#
#         if index == 0:
#
#             self.head = self.head.next
#
#             return
#
#         node = self.get_node(index-1)
#
#         node.next = node.next.next


# linked_list = LinkedList(5)
#
# linked_list.append(12)
#
# linked_list.add_node(0,3)
#
# linked_list.print_all()
#
# linked_list.delete_node(0)
#
# linked_list.print_all()


###.06 링크드리스트 문제

# def _get_linked_list_sum(linked_list):
#
#     linked_list_sum = 0
#
#     head = linked_list.head
#
#     while head is not None:
#
#         linked_list_sum = linked_list_sum * 10 + head.data
#
#         head = head.next
#
#     return linked_list_sum
#
# def get_linked_list_sum(linked_list_1, linked_list_2):
#
#     sum_1 = _get_linked_list_sum(linked_list_1)
#
#     sum_2 = _get_linked_list_sum(linked_list_2)
#
#     return sum_1 + sum_2
#
#
# linked_list_1 = LinkedList(6)
#
# linked_list_1.append(7)
#
# linked_list_1.append(8)
#
# linked_list_2 = LinkedList(3)
#
# linked_list_2.append(5)
#
# linked_list_2.append(4)
#
# print(get_linked_list_sum(linked_list_1, linked_list_2))



###.07 이진탐색

##.ex1

# finding_target = 14
#
# finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
#
# def is_existing_target_number_binary(target, array):
#
#     left = 0
#
#     right = len(array)-1
#
#     while left <= right:
#
#         mid = (left + right) //2
#
#         if array[mid] > target:
#
#             right = mid -1
#
#         elif array[mid] < target:
#
#             left = mid +1
#
#         else:
#
#             return mid
#
#     return -1
#
# # while 조건이 깨지는 경우는 left가 right가 커지는 경우와 right가 left보다 작아지는 경우 오직 2가지 뿐이다. 그런데 이 2가지 경우는 array[mid]가 target보다 크거나 작은 두가지 경우에 의해서 발생되게된다. 즉 mid에서 1을 더하거나 빼는 동작에 의해서 발생하게된다.
# # 따라서, while의 조건 left <- right 을 깨뜨리기 전의 마지막 mid 값이 그나마 찾고자하는 target 값에 언제나 항상 제일 가까운 값이다.
#
# result = is_existing_target_number_binary(finding_target, finding_numbers)
#
# print(result)



###.08 재귀함수_1

# def count_down(number):
#
#     if number <0:
#
#         return
#
#     print(number)          # number를 출력하고
#
#     count_down(number - 1) # count_down 함수를 number - 1 인자를 주고 다시 호출한다!
#
# count_down(60)

# 재귀함수를 사용할 때엔 반드시 재귀함수가 언제 끝날지를 정해줘야한다.


###.09 재귀함수_2

##.ex1

# def factorial(n):
#
#     if n <= 1:
#
#         return 1
#
#     return n * factorial(n-1)
#
# print(factorial(5))

##.ex2

# input = "abcba"
#
# def is_palindrome(string):
#
#     length = len(string)
#
#     for i in range(length):
#
#         if string[i] != string[length-1-i]:
#
#             return False
#
#     return True
#
# print(is_palindrome(input))

##.ex03

# input = "abcba"
#
# def is_palindrome(string):
#
#     if len(string) <=1:
#
#         return True
#
#     if string[0] != string[-1]:
#
#         return False
#
#     return is_palindrome(string[1:-1])
#
# print(is_palindrome(input))


###.숙제

##.ex1

# class Node:
#
#     def __init__(self, data):
#
#         self.data = data
#
#         self.next = None
#
# class LinkedList:
#
#     def __init__(self, value):
#
#         self.head = Node(value)
#
#     def append(self, value):
#
#         cur = self.head
#
#         while cur.next is not None:
#
#             cur = cur.next
#
#         cur.next = Node(value)
#
#     def get_kth_node_from_last(self, k):
#
#         length = 1
#
#         cur = self.head
#
#         while cur.next is not None:
#
#             cur = cur.next
#
#             length += 1
#
#         end_length = length - k
#
#         cur = self.head
#
#         for i in range(end_length):
#
#             cur = cur.next
#
#         return cur
#
#
# linked_list = LinkedList(6)
#
# linked_list.append(7)
#
# linked_list.append(8)
#
# print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!

##.ex1_2

# def get_kth_node_from_last(self, k):
#
#     slow = self.head
#
#     fast = self.head
#
#     for i in range(k):
#
#         fast = fast.next
#
#     while fast is not None:
#
#         slow = slow.next
#
#         fast = fast.next
#
#     return slow
#
#
# linked_list = LinkedList(6)
#
# linked_list.append(7)
#
# linked_list.append(8)
#
# print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!


##.ex2

# def is_existing_target_number_binary(target, array):
#
#     left = 0
#
#     right = len(array)-1
#
#     while left <= right:
#
#         mid = (left + right) //2
#
#         if array[mid] > target:
#
#             right = mid -1
#
#         elif array[mid] < target:
#
#             left = mid +1
#
#         else:
#
#             return mid
#
#     return 0
#
#
# shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
#
# shop_orders = ["오뎅", "콜라", "만두"]
#
# def is_available_to_order(menus, orders):
#
#     shop_menus.sort()
#
# # sort() 메소드는 배열의 길이가 N일때, O(NlogN)의 시간복잡도를 가진다.
#
#     for order in orders:
#
#         if not is_existing_target_number_binary(order,shop_menus):
#
# # 이분탐색의 시간복잡도는 배열의 길이가 N일때 O(logN)으로 결정된다. 그런데 이경우 orders배열의 길이 또한 N이므로, N개에 대해서 logN의 시간복잡도가 발생하기 때문에 최종적으로 O(NlogN)의 시간복잡도가 발생하게된다.
# # 최종적으로 O(NlogN + NlogN) = O(2NlogN) 의 시간복잡도가 발생하므로 시간효율성은 O(NlogN)으로 결정되게된다.
#
#             return False
#
#     return True
#
# result = is_available_to_order(shop_menus, shop_orders)
#
# print(result)


##.ex_2

# shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
#
# shop_orders = ["오뎅", "콜라", "만두"]
#
# def is_available_to_order(menus, orders):
#
#     menus_set = set(menus)
#
# # 배열은 set 자료구조형으로 표현하는데에는 O(N)의 시간이 걸린다.
#
#     for order in orders:
#
#         if order not in menus_set:
#
# # 집합 자료구조 set안에 원소가 있는지 없는지 파악하는 데에는 O(1)의 시간이 소요된다. 그런데 이것을 orders 배열의 길이 N 만큼 반복하므로 결과적으로 O(N)의 시간복잡도가 발생하게된다.
#
#             return False
#
#     return True
#
# # 최종적으로 O(N+N) 의 시간복잡도가 발생하므로 O(N)으로 시간복잡도가 결정된다. 즉, 위의 코드의 시간복잡도가 O(NlogN)인 것에 비해 훨씬 시간효율적인 코드가 된다.
# # 여기에서 알수 있는 것처럼 이분탐색 알고리즘은 매우 효율적인 알고리즘이지만, 경우에 따라서는 훨씬 더 효율적인 알고리즘이 존재할 수 있는 것이다.
#
# result = is_available_to_order(shop_menus, shop_orders)
#
# print(result)


##.ex_3

# numbers = [2,3,1]
#
# result = []
#
# def get_count(array, index, sum, result):
#
#     if index == len(array):
#
#         result.append(sum)
#
#         return result
#
#     get_count(array, index+1, sum+array[index], result)
#
#     get_count(array, index+1, sum-array[index], result)
#
#
# print(get_count(numbers,0,0,result))

# 이 코드의 결과는 최초의 get_count 함수에 의해 발생된 결과값에 의해서 8번의 return이 발생하게된다. 즉, 최초의 함수 get_count에 대하여 하나의 return을 특정할 수 가 없는 경우가 되므로 최종적인 하나의 return값을 print하여 보여달라는 결과는 None으로 결정되게된다.


# numbers = [2,3,1]
#
# result = []
#
# def get_count(array, index, sum, result):
#
#     if index == len(array):
#
#         result.append(sum)
#
#         return print(result)
#
#     get_count(array, index+1, sum+array[index], result)
#
#     get_count(array, index+1, sum-array[index], result)
#
# print(get_count(numbers,0,0,result))

# 첫번째 경우와 다르게 return에 print을 집어넣으면 다음과 같이


# numbers = [1,1,1,1,1]
#
# target = 3
#
# count_answer = 0
#
# result = []
#
# def get_count(array, index, sum, result, target):
#
#     if index == len(array):
#
#         if sum == target:
#
#             global count_answer
#
#             count_answer += 1
#
#         return
#
#     get_count(array, index+1, sum+array[index], result, target)
#
#     get_count(array, index+1, sum-array[index], result, target)
#
# get_count(numbers, 0, 0, result, target)
#
# print(count_answer)



