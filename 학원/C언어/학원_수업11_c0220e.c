#include <stdio.h>

main(){

    int num;

    int s = 0;

    printf("�����Է�:");

    scanf(" %d",&num);

    while(num>0){

        s = s+num;

        num = num -1;

    }

    printf("�� �հ�:%d",s);

    return 0;

}
