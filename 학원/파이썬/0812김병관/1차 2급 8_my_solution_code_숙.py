def solution(sentence):
    str1 = ''
    for c in sentence:
        if c != '.' and c != ' ':
            str1 += c
    size = len(str1)
    for i in range(size):
        if str1[i] != str1[size - 1 - i]:
            return False
    return True


sentence1 = "never odd or even."
ret1 = solution(sentence1)
print(ret1)
    
sentence2 = "palindrome"
ret2 = solution(sentence2)
print(ret2)
