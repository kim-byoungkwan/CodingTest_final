#include <stdio.h>

main(){

    int i;

    int num;

    int fac = 1;

    printf("�����Է�:");

    scanf("%d",&num);


    for(i=1;i<=num;i++){

        fac = fac*i;

    }

    printf("%d���丮��:%d",num,fac);

    return 0;

}


