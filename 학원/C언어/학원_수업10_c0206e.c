#include <stdio.h>

main(){

    int x,y;

    int large,small;


    printf("정수 2개를 입력하세요:");

    scanf(" %d %d",&x,&y);


    large = x > y ? x : y;

    // x가 y보다 큰 것이 참이면 x를 출력하여 large 변수에 할당하고,
    // x가 y보다 큰 것이 거짓이면, y를 출력하여 large 변수에 할당한다는 의미이다.

    small = x > y ? y : x;

    printf("큰 수는 %d \n",large);

    printf("작은 수는 %d \n",small);


    return 0;

}


