#include <stdio.h>

main(){

    int i = 7;

    char name[] = "abcde fghij";


    printf("%d\n",sizeof(i));

    printf("%d\n",sizeof(name));

    printf("%d",strlen(name));


    return 0;

}

// int ������ ũ��� 4byte �̹Ƿ� ���� i�� ũ�⵵ sizeof�� ���� 4�� �����ȴ�.

// �迭 name�� ũ�⿣ ���ڿ��� ���� �ǹ��ϴ� null�� ���ԵǾ� +1 �� ���·�
// ����� 12�� ��µȴ�

