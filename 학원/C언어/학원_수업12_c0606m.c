#include <stdio.h>

int g1 = 10;

// 위와 같은 전역변수는 반드시 main() 함수 앞에 정의되어야만 한다.


main(){

    float n1;

    n1=9.0;

    printf("%d %.2f\n",g1,n1);

    f_again();

    return 0;

}

float g2 = 19.0;

f_again(){

    int n2 = 5;

    printf("%d %.2f %d\n",n2,g2,g1);

    return;

}



