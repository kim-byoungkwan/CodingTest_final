#include <stdio.h>

// scanf는 어떠한 변수의 주소공간에 값을 할당 받아 그 어떠한 변수에 값을
// 할당하는 과정이므로, 본질적으로 scanf에 할당받을 주소공간에 해당하는
// 변수가 미리 존재해야한다.

main(){

int card;

printf("숫자카드 번호 입력:");

scanf("%d",&card);

if(card <= 13){

    printf("스페이드");

}else if(card <= 26){

    printf("다이아몬드");

}else if(card <= 39){

    printf("하트");

}else if(card <= 52){

    printf("클로버");

}else{

    printf("에러");

}

return 0;

}


