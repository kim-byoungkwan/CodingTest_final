#include <stdio.h>

main(){

    int value = 42;

    int * pX;

    int * pY;


    pX = &value;

    pY = &value;

    // 위에서 px,py는 포인터 변수 이므로, &value는 '202dd02j3' 와같은
    // 실질적인 주소명을 표현하고,

    *pX = 15;

    // 위의 포인터 변수 px 앞에 *이 붙은 것은 실제 px 가 지칭하는 주소공간
    // value안에 할당되어 있는 실질적인 값을 의미하는데, 이 값을 15로 변경
    // 한 것이다.

    // 즉, 이제 int value = 15;인 상태인 것이다.

    printf("%d\n",*pX);

    printf("%d",*pY);

    return 0;

}

