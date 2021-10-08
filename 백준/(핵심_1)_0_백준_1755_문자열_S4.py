M,N = map(int,input().split())

dict_standard = {
        0:"zero",
        1:'one',
        2:'two',
        3:'three',
        4:'four',
        5:'five',
        6:'six',
        7:'seven',
        8:'eight',
        9:'nine'
}

dict_real = {}


for i in range(M,N+1):

    k = i

    result = []

    while i:

        result.append(dict_standard[i % 10])

        i = i // 10

    dict_real[k] = ''.join(result[::-1])


answer = sorted(dict_real.items(),key= lambda x : x[1])

count = 0

for end in answer:

    count += 1

    if count % 10 == 0:

        print(end[0])

    else:

        print(end[0],end=' ')
