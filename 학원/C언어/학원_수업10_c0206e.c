#include <stdio.h>

main(){

    int x,y;

    int large,small;


    printf("���� 2���� �Է��ϼ���:");

    scanf(" %d %d",&x,&y);


    large = x > y ? x : y;

    // x�� y���� ū ���� ���̸� x�� ����Ͽ� large ������ �Ҵ��ϰ�,
    // x�� y���� ū ���� �����̸�, y�� ����Ͽ� large ������ �Ҵ��Ѵٴ� �ǹ��̴�.

    small = x > y ? y : x;

    printf("ū ���� %d \n",large);

    printf("���� ���� %d \n",small);


    return 0;

}


