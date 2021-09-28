dict = {
        'black':[0,1],
        'brown':[1,10],
        'red':[2,100],
        'orange':[3,1000],
        'yellow':[4,10000],
        'green':[5,100000],
        'blue':[6,1000000],
        'violet':[7,10000000],
        'grey':[8,100000000],
        'white':[9,1000000000]
}


value_1 = input()

value_2 = input()

value_multi = input()


result_former = str(dict[value_1][0]) + str(dict[value_2][0])

result_former = int(result_former)

print(result_former*dict[value_multi][1])
