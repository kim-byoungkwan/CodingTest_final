#include <stdio.h>

main(){

int num;

printf("1에서 10사이 숫자 입력:");

scanf(" %d,&num");

if(num >= 5 && num % 2 != 0){

    printf("5이상의 홀수 입니다.");

}else{

printf("5미만이거나 짝수 입니다.");

}
return 0;
}


// 본질적으로 main() 함수의 앞과 인수에는 int main(void) 이와 같은 요소가 생략되어있다.
// 따라서 반드시 return 값이 존재해야하는 함수의 정의역과 치역의 본질상 어떠한 return값이
// 반드시 존재해야하는데, 이경우 main함수의 원래의 함수형은 int 이므로 임의의 int 값인
// 0을 돌려주는 것이다.
