#include <stdio.h>
#define SIZE 5

main(){

    int values[SIZE];

    int i,s;

    float a;

    for(i=0;i<SIZE;i++){

        printf("점수 입력:");

        scanf("%d",&values[i]);

    }

    s=0;

    for(i=0;i<SIZE;i++){

        s = s+values[i];

    }

    a=s/SIZE;

    printf("합계:%d\n",s);

    printf("평균:%.1f",a);

    return 0;

}




