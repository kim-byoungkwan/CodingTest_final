#include <stdio.h>

main(){

    int ages[3];

    int i;


    for(i=0;i<3;i++){

        printf("%d��° �ڳ� ����:",i+1);

        scanf("%d",&ages[i]);

    }

    for(i=0;i<3;i++){

        printf("%d��° �ڳ� ����:%d\n",i+1,ages[i]);

    }

    return 0;
}
