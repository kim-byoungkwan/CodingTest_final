#include <stdio.h>

main(){

    int value = 42;

    int * pX;

    int * pY;


    pX = &value;

    pY = &value;

    // ������ px,py�� ������ ���� �̹Ƿ�, &value�� '202dd02j3' �Ͱ���
    // �������� �ּҸ��� ǥ���ϰ�,

    *pX = 15;

    // ���� ������ ���� px �տ� *�� ���� ���� ���� px �� ��Ī�ϴ� �ּҰ���
    // value�ȿ� �Ҵ�Ǿ� �ִ� �������� ���� �ǹ��ϴµ�, �� ���� 15�� ����
    // �� ���̴�.

    // ��, ���� int value = 15;�� ������ ���̴�.

    printf("%d\n",*pX);

    printf("%d",*pY);

    return 0;

}

