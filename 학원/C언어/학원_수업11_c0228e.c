#include <stdio.h>

main(){

    int num1,num2,result;

    char flag;

    flag = 'N';

    do{

        printf("ù��° �����Է�:");

        scanf("%d",&num1);

        printf("�ι�° �����Է�:");

        scanf("%d",&num2);

        result = num1*num2;

        printf("%d * %d = %d\n",num1,num2,result);

        printf("���������� �����Ͻðڽ��ϱ�? Y/N:");

        scanf(" %c",&flag);

    }while(flag != 'Y');

    return 0;
}


