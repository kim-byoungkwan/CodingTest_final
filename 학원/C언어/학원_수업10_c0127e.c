#include <stdio.h>

main(){

int menu;

printf("�޴��� ������ \n");

printf("1:¥��� 2:«�� 3:�쵿 4:������");

scanf("%d",&menu);

switch(menu){

case(1):printf("¥����� �����߽��ϴ�. \n");

    break;

case(2):printf("«���� �����߽��ϴ�. \n");

    break;

case(3):printf("�쵿�� �����߽��ϴ�.\n");

    break;

case(4):printf("�������� �����߽��ϴ�.\n");

    break;

default:printf("�ش�޴��� �����ϴ�. \n");

    break;

}

return 0;

}

