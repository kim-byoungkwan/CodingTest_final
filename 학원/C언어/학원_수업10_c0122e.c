#include <stdio.h>

main(){

printf("수를 입력하시오:");

int num_1;

scanf("%d",&num_1);

int num_2;

printf("수를 입력하시오:");

scanf("%d",&num_2);

if(num_1 - num_2 == 1 || num_2 - num_1 ==1){

    printf("두 수는 연속된 수 입니다.");

}else{

    printf("두 수는 연속된 수가 아닙니다.");

}

return 0;

}



