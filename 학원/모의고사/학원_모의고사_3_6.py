dict = {

    (0,1) : -1,

    (0,2) : 3,

    (1,2) : -1,

    (1,0) : 3,

    (2,0) : -1,

    (2,1) : 3,

    (0,0) : 0,

    (1,1) : 0,

    (2,2) : 0

}




def solution(recordA,recordB):

    count = 0

    for i in range(len(recordA)):

        temp = (recordA[i], recordB[i])

        count += dict[temp]

        if count <= 0:

            count =0

        else:

            continue

    return count

recordA = [2,0,0,0,0,0,1,1,0,0]

recordB = [0,0,0,0,2,2,0,2,2,2]


print(solution(recordA,recordB))

