def solution(s):

    result = ''

    set = set()

    state = True

    for i in s:

        i = str(i)

        if i == '1':

            state = True

        else:

            state = False

        if state:

            if set:

                result += set.pop()

                result += i

            else:

                result += i

        else:

            set.add(i)
    if set:

        result += set.pop()

    return result


s = '101100011100'