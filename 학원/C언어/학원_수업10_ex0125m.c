#include <stdio.h>

main(){

int card1;

int card2;

int shape1;

int shape2;

printf("숫자카드1 입력:");

scanf("%d",&card1);

printf("숫자카드2 입력:");

scanf("%d",&card2);

shape1 = (card1 - 1) / 13;

shape2 = (card2 - 1) / 13;

if(shape1 == shape2){

    printf("같은 모양 입니다.");

}else{

printf("다른 모양 입니다.");

}

return 0;

}

