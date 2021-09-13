#include <stdio.h>

main(){

    int num1,num2,result;

    char flag;

    flag = 'N';

    do{

        printf("첫번째 숫자입력:");

        scanf("%d",&num1);

        printf("두번째 숫자입력:");

        scanf("%d",&num2);

        result = num1*num2;

        printf("%d * %d = %d\n",num1,num2,result);

        printf("곱셈연산을 종료하시겠습니까? Y/N:");

        scanf(" %c",&flag);

    }while(flag != 'Y');

    return 0;
}


