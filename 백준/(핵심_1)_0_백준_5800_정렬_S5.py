K = int(input())

for i in range(K):

    class_x = sorted(list(map(int,input().split()))[1:],reverse=True)

    gap_class_x = []

    for j in range(1,len(class_x)):

        gap = class_x[j-1] - class_x[j]

        gap_class_x.append(gap)

    print("Class {}".format(i+1))

    print("Max {}, Min {}, Largest gap {}".format(class_x[0],class_x[-1],max(gap_class_x)))
