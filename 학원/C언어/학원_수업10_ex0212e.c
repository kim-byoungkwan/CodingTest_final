#include <stdio.h>

main(){

    int num;

    int sum = 0;

    printf("���ڸ� �Է��Ͻÿ�:\n");

    for(num=1;num<=10;num++){

        if(num % 2 !=0){

            sum = sum + num;

        }

    }

    printf(" %d",sum);

    return 0;

}
