#include <stdio.h>

// 주소로 전달하기

main(){

    int i;

    printf("정수 입력:");

    scanf(" %d",&i);

    half(&i);

    printf("%d",i);

    return 0;

}

half(int * i){

    // 위의 함수 인수 정의에서 이미 i는 포인터 변수로 정의되었으므로,
    // i 만으로 주소값을 표현할 수 있다.
    // 그러므로, 아래의 i에 *를 붙여준 *i 는 본질적으로 **i 와 같은 경우로
    // i가 표현하는 주소값에 해당하는 값을 출력하게 된다.

    *i = *i/2;

    // 위의 과정에서 변수 i의 본질적인 값이 바뀌게 된다.

    printf("%d\n",*i);

    return;

}



