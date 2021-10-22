from collections import deque

import copy

N = int(input())

box = []

for i in range(N):

    string = input()

    word = deque(string)

    for _ in range(len(word)):

        word.rotate(1)

        word_temp = list(copy.deepcopy(word))

        box.append(word_temp)

