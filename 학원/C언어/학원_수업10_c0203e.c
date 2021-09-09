#include <stdio.h>

main(){

    int i=4, j=6, n;

    n = i++ * j;

    printf("i=%d \n",i);

    printf("n=%d",n);

    return 0;

}

// i++ 의 의미는 i를 먼저 사용하고 i에 1을 더해주는 연산을 취해 i를
// 변경해주는 것이다.

