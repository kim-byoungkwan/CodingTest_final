word = ''

while True:

    try:

        word = word + input()

    except:

        break

print(sum(map(int,word.split(','))))


##.Q

##.이런경우에 except 종결조건을 어떻게 실행시켜 break를 하는 것일까? 즉, EOF(파일의 끝)을 만난다는 것은 무엇을 의미하는가?