def solution(expression):

    if '+' in expression:

        expression = expression.split('+')

        expression = list(map(int,expression))

        return expression[0] + expression[1]

    elif '-' in expression:

        expression = expression.split('-')

        expression = list(map(int, expression))

        return expression[0] - expression[1]

    elif '*' in expression:

        expression = expression.split('*')

        expression = list(map(int, expression))

        return expression[0] * expression[1]


expression = '123+12'

print(solution(expression))
