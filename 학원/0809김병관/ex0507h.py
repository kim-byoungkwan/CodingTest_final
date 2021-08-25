s_count = int(input("학생수 입력:"))

scores = []
arr_name = []
while not len(scores) == s_count:
    name = input("이름 입력:")
    score = int(input("점수 입력:"))
    print("----------------------------------")
    arr_name.append(name)
    scores.append(score)

sum = 0
seq = 0
for s in scores:
    sum = sum + s
    rank = 1
    for s2 in scores:
        if s < s2:
            rank = rank + 1
    print("%s학생의 점수는 %d점이고 등수는 %d등 입니다."%(arr_name[seq],s,rank))
    seq = seq + 1

print("================================================")
print("전체 학생 점수의 평균은",sum/s_count,"점 입니다.")
