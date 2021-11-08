def solution(money):

    count = 0

    while money:

        if money // 1000 > 0:

            count += money // 1000

            money = money % 1000

        elif money // 500 >0:

            count += money // 500

            money = money % 500

        elif money // 100 >0:

            count += money // 100

            money = money % 100

        elif money // 50 >0:

            count += money // 50

            money = money % 50

        else:

            count += money // 10

            money = money % 10

    return count


money = 2760


print(solution(money))
