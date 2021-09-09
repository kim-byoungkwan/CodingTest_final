#include <stdio.h>

main(){

    int num;

    int sum = 0;

    printf("숫자를 입력하시오:\n");

    for(num=1;num<=10;num++){

        if(num % 2 !=0){

            sum = sum + num;

        }

    }

    printf(" %d",sum);

    return 0;

}
