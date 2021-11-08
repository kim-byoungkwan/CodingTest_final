def solution(password):

    result = True

    for i in range(2,len(password)):

        if abs(ord(password[i-2]) - ord(password[i-1])) == 1 and abs(ord(password[i-1])-ord(password[i])) == 1:

            result = False

        else:

            continue

    return result


password_1 = 'cospro890'

password_2 = 'cba323'


print(solution(password_2))



