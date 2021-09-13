#include <stdio.h>

main(){

    int ages[3];

    int i;


    for(i=0;i<3;i++){

        printf("%d번째 자녀 나이:",i+1);

        scanf("%d",&ages[i]);

    }

    for(i=0;i<3;i++){

        printf("%d번째 자녀 나이:%d\n",i+1,ages[i]);

    }

    return 0;
}
