#include <stdio.h>

main(){

    int i;

    int money;

    int year;

    float interest_rate;


    printf("���� �Է�:");

    scanf("%d",&money);

    printf("�� �Է�:");

    scanf("%d",&year);

    printf("�� ����(%%) �Է�:");

    scanf("%f",&interest_rate);


    for(i=1;i<=year;i++){

        money = money + (money * (interest_rate/100));

        printf("%d�� �� �ݾ���:%d\n",i,money);

    }

    printf("���� ã�� �� �ݾ���:%d",money);

    return 0;

}


