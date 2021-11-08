import sys

T = int(sys.stdin.readline())

for _ in range(T):

    a,b = map(int,sys.stdin.readline().split())

    word = sys.stdin.readline()

    result = ''

    for i in word:

        temp = ord(i)-65

        temp_2 = (temp*a +b) % 26

        result += chr(temp_2+65)

    print(result)
