def solution(korean,english):

    math = 210 - (korean + english)

    if math > 100:

        return -1

    else:

        return math


korean = 70

english = 60

print(solution(korean,english))