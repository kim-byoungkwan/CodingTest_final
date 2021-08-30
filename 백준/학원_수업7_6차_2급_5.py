def solution(money,price,n):

    output = (money // price)

    rest = output + (money % price)

    while rest != 0:

    

    output = 0

    rest = 0

    output = output + (money // price)

    rest = rest + (money % price)

    output = output + (output // n)

    rest = rest + (output % n)





