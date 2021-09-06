#include <stdio.h>

main(){

int a;

char b;

char c[10];

printf("숫자 입력:");

scanf("%d", &a);

printf("%d \n",a);


printf("문자 입력:");

scanf(" %c", &b);

// scanf("%c", &b); 로 하면 에러가 발생한다(엔터의 영향)
// 즉 %c 라는 변수형은 1개의 문자만 받는 다는 것을 의미하는데,
// 엔터도 본질적으로는 \n 이라는 하나의 문자이므로 c에 \n 이 할당되어
// 정작 할당하고자 하는 문자를 할당하지 못하게 되는 것이다.


printf("%c \n",b);


printf("문자열 입력:");

scanf("%s",c); // 배열은 주소공간에 값을 따로 전달할 필요없다.

// scanf에서 %s 는 내가 입력 받을 문자의 형태를 표현한다.
printf("%s",c);

return 0;

}


