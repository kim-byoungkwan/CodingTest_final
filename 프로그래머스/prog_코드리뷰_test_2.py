import sys

input = sys.stdin.readline

def solution(s):

    stack = []

    for i in s:

        if i == '(':

            stack.append(i)

        else:

            if stack:

                if stack[-1] == '(':

                    stack.pop()

                else:

                    return False

            else:

                return False

    if stack:

        return False

    else:

        return True


s = "(())()"

print(solution(s))


