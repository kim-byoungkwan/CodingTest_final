#include <stdio.h>

main(){

    int i = 7;

    char name[] = "abcde fghij";


    printf("%d\n",sizeof(i));

    printf("%d\n",sizeof(name));

    printf("%d",strlen(name));


    return 0;

}

// int 변수의 크기는 4byte 이므로 변수 i의 크기도 sizeof에 의해 4로 결정된다.

// 배열 name의 크기엔 문자열의 끝을 의미하는 null이 포함되어 +1 된 상태로
// 결과가 12로 출력된다

