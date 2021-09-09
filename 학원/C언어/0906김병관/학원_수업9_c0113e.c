#include <stdio.h>

main(){

char name[20]; // 배열은 포인터가 필요없다. 왜냐하면 배열의 이름을 표현하는 name 그 자체가 주소를 표현하는 포인터를 의미하기 때문이다.

int age;

char hakjum;

printf("성명 입력:");

scanf(" %s",name);

printf("성명은 %s \n",name);


printf("나이 입력:");

scanf(" %d", &age); // age라는 int형 변수가 정의 됐고, 그 변수의 값이 할당되는 곳의 주소를 표현하는 주소 공간인 &age에 scanf를 통해 값을 받아서,
                    // 변수 age에 값을 할당하는 것이다. 즉, scanf는 &에 의해 표현된 주소공간에 주소 택을 붙여주는 동작과, 그 주소가 표현하는 위치에 값을 전달하는
                    // 역할이라고 생각하면 된다.

printf("나이는 %d \n",age);


printf("학점 입력:");

scanf(" %c",&hakjum);

printf("학점은 %c\n",hakjum);

return 0;


}

