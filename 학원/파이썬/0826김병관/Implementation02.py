# 문자열 재정렬

# 알파벳 대문자와 숫자로만 구성된 문자열이 입력으로 주어진다.
# 이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에
# 그 뒤에 모든 숫자를 더한 값을 이어서 출력한다.
# 예) 입력: K1KA5CB7    출력: ABCKK13

data = input()
result = []
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value = value + int(x)

result.sort()

if value != 0:
    result.append(str(value))

print(''.join(result))
