#include <stdio.h>

main(){

int card1;

int card2;

int shape1;

int shape2;

printf("����ī��1 �Է�:");

scanf("%d",&card1);

printf("����ī��2 �Է�:");

scanf("%d",&card2);

shape1 = (card1 - 1) / 13;

shape2 = (card2 - 1) / 13;

if(shape1 == shape2){

    printf("���� ��� �Դϴ�.");

}else{

printf("�ٸ� ��� �Դϴ�.");

}

return 0;

}

