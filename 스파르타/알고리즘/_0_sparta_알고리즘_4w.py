###.4 힙

##.ex1

# class MaxHeap:
#
#     def __init__(self):
#
#         self.items = [None]
#
# # 1번노드를 1번 인덱스에 대응시키기 위해서 힙을 구성하는 배열을 생성하자 마자 None 값을 0번 인덱스에 포함되도록 한다.
#
#     def insert(self, value):
#
#         self.items.append(value)
#
#         cur_index = len(self.items) -1
#
#         while cur_index >1:
#
#             parent_index = cur_index //2
#
#             if self.items[cur_index] > self.items[parent_index]:
#
#                 self.items[cur_index],self.items[parent_index] = self.items[parent_index],self.items[cur_index]
#
#                 cur_index = parent_index
#
#             else:
#
#                 break
#
# # 완전이진트리 이므로 새로운 값의 추가는 항상 맨 마지막 빈 공간에 추가되기때문에 부모노드보다 작은 노드일 경우 바로 break걸어줘도 된다. 왜냐하면 새롭게 추가된 노드는 항상 맨마지막 빈 공간에서부터 출발했기 때문에 부모노드보다 작은 순간은 항상 최소값이 발생된 최초의 순간이기 때문이다.
#         return
#
# # 완전이진트리에서 존재하는 모든 노드의 수를 N으로 표현할 때, 완전이진트리의 높이 h는 log(N)으로 결정된다. 즉, 어떠한 새로운 노드가 추가될 때 발생될 수 있는 최대의 교환작업의 수는 맨 끝 노드 공간에서 루트노드 공간까지 올라가는 경우이다. 즉, 높이 만큼 반복되는 경우이다.
# # 그러므로 힙에서 교환동작이 최대한 발생하는 시간복잡도는 모든 노드의 수가 N 일때의 높이인 O(logN)으로 결정되게 된다.
#
#     def delete(self):
#
#         self.items[1],self.items[-1] = self.items[-1],self.items[1]
#
#         prev_max = self.items.pop()
#
#         cur_index = 1
#
#         while cur_index <= len(self.items)-1:
#
#             left_child_index = cur_index*2
#
#             right_child_index = cur_index*2+1
#
#             max_index = cur_index
#
# # max_index에는 부모노드와 두개의 자식노드중의 가장 큰 값을 갖는 노드의 인덱스가 저장되게된다. 즉, 3개중에 가장 큰 노드가 저장되어있는 것이다.
#
#
#             if left_child_index <= len(self.items) -1 and self.items[left_child_index] > self.items[max_index]:
#
#                 max_index = left_child_index
#
#             if right_child_index <= len(self.items) -1 and self.items[right_child_index] > self.items[max_index]:
#
#                 max_index = right_child_index
#
#             if max_index == cur_index:
#
#                 break
#
#             self.items[cur_index],self.items[max_index] = self.items[max_index],self.items[cur_index]
#
#             cur_index = max_index
#
#         return prev_max
#
# max_heap = MaxHeap()
#
# max_heap.insert(8)
#
# max_heap.insert(6)
#
# max_heap.insert(7)
#
# max_heap.insert(2)
#
# max_heap.insert(5)
#
# max_heap.insert(4)
#
# print(max_heap.items)  # [None, 8, 6, 7, 2, 5, 4]
#
# print(max_heap.delete())  # 8 을 반환해야 합니다!
#
# print(max_heap.items)  # [None, 7, 6, 4, 2, 5]



###.6 BFS & DFS

##.ex1

# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
# graph = {
#     1: [2, 5, 9],
#     2: [1, 3],
#     3: [2, 4],
#     4: [3],
#     5: [1, 6, 8],
#     6: [5, 7],
#     7: [6],
#     8: [5],
#     9: [1, 10],
#     10: [9]
# }
#
# visited = []
#
# def dfs_recursion(adjacent_graph, cur_node, visited_array):
#
#     visited_array.append(cur_node)
#
#     for adjacent_node in adjacent_graph[cur_node]:
#
#         if adjacent_node not in visited_array:
#
# # 위의 if 조건이 일종의 재귀함수의 탈출조건으로 기능한다.
#
#             dfs_recursion(adjacent_graph, adjacent_node, visited_array)
#
#     return
#
# dfs_recursion(graph, 1, visited)  # 1 이 시작노드입니다!
#
# print(visited)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 이 출력되어야 합니다!


##.ex2

# graph = {
#     1: [2, 5, 9],
#     2: [1, 3],
#     3: [2, 4],
#     4: [3],
#     5: [1, 6, 8],
#     6: [5, 7],
#     7: [6],
#     8: [5],
#     9: [1, 10],
#     10: [9]
# }
#
#
# def dfs_stack(adjacent_graph, start_node):
#
#      visited = []
#
#      stack = []
#
#      stack.append(start_node)
#
#      while stack:
#
#          current_node = stack.pop()
#
#          visited.append(current_node)
#
#          for adjacent_node in adjacent_graph[current_node]:
#
#              if adjacent_node not in visited:
#
#                  stack.append(adjacent_node)
#
#      return visited
#
#
# print(dfs_stack(graph, 1))  # 1 이 시작노드입니다!

# [1, 9, 10, 5, 8, 6, 7, 2, 3, 4] 이 출력되어야 합니다!

# dfs를 재귀로 구현하는 방법과 stack로 구현하는 방법에서 본질적으로 동일한 부분은 재귀에선 for문의 요소값이 실행될 때, 재귀가 발생하면 뒤에 이어지는 for문의 요소값이 보류된채로 재귀함수가 실행되는 순간과, stack에선 인접노드를 stack에 넣을 때, 맨위에 값이 출력되고, 인접노드 값은 스택에 저장되어 있는 순간이다.

# 또한 본질적으로 인접된 노드와의 연결성을 구현하는 것은 재귀적인 방법이나 stack 방법이나 모두 for문에서 리스트의 모든 요소값을 순차적으로 실행하는 방법으로 구현한다.


###.7 BFS

# graph = {
#     1: [2, 3, 4],
#     2: [1, 5],
#     3: [1, 6, 7],
#     4: [1, 8],
#     5: [2, 9],
#     6: [3, 10],
#     7: [3],
#     8: [4],
#     9: [5],
#     10: [6]
# }
#
# def bfs_queue(adj_graph, start_node):
#
#     queue = [start_node]
#
#     visited = []
#
#     while queue:
#
#         current_node = queue.pop(0)
#
#         visited.append(current_node)
#
#         for adjacent_node in graph[current_node]:
#
#             if adjacent_node not in visited:
#
#                 queue.append(adjacent_node)
#
#     return visited
#
# print(bfs_queue(graph, 1))  # 1 이 시작노드입니다!

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 이 출력되어야 합니다!



###.8 다이나믹프로그래밍


##.ex1

# input = 20
#
# def fibo_recursion(n):
#
#     if n <=2:
#
#         return 1
#
#     return fibo_recursion(n-1) + fibo_recursion(n-2)
#
# print(fibo_recursion(input))  # 6765


##.ex2

# input = 100
#
# # memo 라는 변수에 Fibo(1)과 Fibo(2) 값을 저장해놨습니다!
#
# memo = {
#     1: 1,
#     2: 1
# }
#
# def fibo_dynamic_programming(n, fibo_memo):
#
#     if n in fibo_memo:
#
#         return fibo_memo[n]
#
#     nth_fibo = fibo_dynamic_programming(n-1,fibo_memo) + fibo_dynamic_programming(n-2,fibo_memo)
#
#     fibo_memo[n] = nth_fibo
#
#     return fibo_memo[n]
#
# print(fibo_dynamic_programming(input, memo))



###.9 숙제

##.ex1

import heapq

ramen_stock = 4

supply_dates = [4, 10, 15]

supply_supplies = [20, 5, 10]

supply_recover_k = 30

def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):


    return

print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))
















##.ex2



##.ex3




















