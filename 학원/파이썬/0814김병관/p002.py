arr = []
arr2 = []

Tc = int(input("테스트 케이스 수 입력:"))

while Tc > 0:
    num = int(input("숫자입력:"))
    tmp = num
    reverseNum = 0
    s = 0
    while tmp != 0:
        reverseNum = reverseNum * 10 + tmp % 10
        tmp = tmp // 10
    s = num + reverseNum

    tmp = s
    #한자리씩 배열에 저장
    while tmp > 0:
        arr.append(tmp % 10)
        arr2.append(tmp % 10)
        tmp = tmp // 10
        
    flag = 1
    #회문인지 판단
    while arr:
        if arr.pop(0) != arr2.pop():
            flag = 0
            break

    if flag == 1:
        print("yes")
    else:
        print("no")

    Tc = Tc - 1
