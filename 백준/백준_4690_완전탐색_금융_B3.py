for i in range(6,101):

    for j in range(2,101):

        for m in range(j+1,101):

            for n in range(m+1,101):

                if i*i*i == j*j*j + m*m*m + n*n*n:

                    a = i
                    b = j
                    c = m
                    d = n

                    print("Cube = {}, Triple = ({},{},{})".format(a,b,c,d))

                if i*i*i < j*j*j + m*m*m + n*n*n:

                    break
