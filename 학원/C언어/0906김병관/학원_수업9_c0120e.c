#include <stdio.h>

main(){

int num;

printf("숫자 입력:");

scanf("%d",&num);

if(num % 2 == 0){

    printf("%d: 짝수입니다.\n",num);

}else{

    printf("%d: 홀수입니다.\n",num);

}

return 0;

}



