#include <stdio.h>

main(){

int num;

printf("1에서 10사이 숫자 입력:");

scanf(" %d",&num);

if(num >= 5 && num % 2 != 0){

    printf("5이상의 홀수 입니다.");

}else{

printf("5미만이거나 짝수 입니다.");

}

return 0;

}

