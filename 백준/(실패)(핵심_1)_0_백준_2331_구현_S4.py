def fuction(A,P):

    box = 0

    while A:

        residual = A % 10

        A = A // 10

        box += residual**P


