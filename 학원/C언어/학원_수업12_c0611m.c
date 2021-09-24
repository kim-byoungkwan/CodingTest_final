#include <stdio.h>

changesome(int i,float * newX,int iArr[5]);

// 위 처럼 앞으로 호출할 함수에 대하여 미리 표현해놓는 것은 함수 원형이라고 한다.

main(){

    int i = 10;

    int ctr;

    float x = 20.2;

    int iArr[5]={10,20,30,40,50};


    printf("함수를 호출하기 전의 변수값:\n");

    printf("i = %d\n",i);

    printf("x=%.1f\n",x);

    for(ctr = 0;ctr<5;ctr++){

        printf("iArr[%d] = %d\n",ctr,iArr[ctr]);

    }

    // 위의 iArr[] 배열의 요소값은 최초의 요소값으로 출력되게 된다.

    changesome(i,&x,iArr);

    printf("함수를 호출한 후의 변수값:\n");

    printf("i=%d\n",i);

    printf("x=%.if\n",x);

    for(ctr=0;ctr<5;ctr++){

        printf("iArr[%d]=%d\n",ctr,iArr[ctr]);

        // 이때의 iArr[]의 요소값은 위의 changesome 함수가 실행된 뒤의 요소 값이 덮어 씌어진
        // 뒤의 값이므로, 최초에 정의된 요소값과 다르다.

    }

    return 0;

}

changesome(int i,float * newX,int iArr[5]){

    int j;

    i = 11;

    *newX=30.3;

    // chagnesome 함수를 정의할 때 인수에서 이미 newX 변수는 포인터 변수로 정의되었으므로,
    // *표시 없이 newX 만으로 이미 주소값을 표현하는데, 위에선 *를 붙여서 표현하였으므로,
    // newX 가 가리키는 주소에 대응되는 값을 의미하고, 그 값에 30.3이 할당되었으므로, 결과적으로
    // changesome 함수의 두번째 인수엔 항상 30.3 으로 값이 덮어 씌어지게된다.

    for(j=0;j<5;j++){

        iArr[j] = 1+10*j;

    }

    return;

}

