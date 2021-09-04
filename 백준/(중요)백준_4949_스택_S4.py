stack = []

box = []

while True:

    sentence = input()

    if sentence != '.':

        for i in sentence:

            if stack:

                if i == '(' or i =='[':

                    stack.append(i)

                elif i == ')':

                    if stack[-1] == '(':

                        stack.pop()

                    else:

                        box.append('no')

                elif i == ']':

                    if stack[-1] == '[':

                        stack.pop()

                    else:

                        box.append('no')

                else:

                    continue

            else:

                if i == '(' or i == '[':

                    stack.append(i)

                elif i == ')' or i == ']':

                    box.append('no')

                    break

                else:

                    continue

        if stack:

            box.append('no')

            stack = []

        else:

            box.append('yes')

            stack = []

        if 'no' in box:

            print('no')

            box = []

        else:

            print('yes')

            box = []

    else:

        break

