#include <stdio.h>

main(){

    int num;

    int tot;


    printf("숫자입력:");

    scanf(" %d",&num);

    tot = f_sum(num);

    printf("총합:%d",tot);

    return 0;

}


f_sum(int num){

    int i;

    int tot=0;

    for(i=1;i<=num;i++){

        tot = tot +i;

    }

    return tot;

}

// f_sum 과 같은 함수의 정의과정에서 사용된 자료형과 그의 변수는 단지 함수의 매커니즘을 표현할 뿐이지
// 실제 변수값의 생성을 의미하지 않는다.
// 따라서, 실제 변수 값을 사용하여 실제 값을 출력하는 main() 함수에서는 생성된 f_sum 함수의 인수를
// 정의해야만 f_sum 함수 매커니즘을 이용하여 실제 값을 도출할 수 있다.
