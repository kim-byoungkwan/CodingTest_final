#include <stdio.h>

// ������ �����ϴ� ��Ŀ����

main(){

    int i;

    printf("���� �Է�:");

    scanf(" %d",&i);

    half(i);

    printf("%d",i);

    return 0;

}

half(int i){

    i = i/2;

    printf("%d\n",i);

    return;

}




