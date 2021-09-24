#include <stdio.h>

main(){

    int point=100;

    int num;

    char * pContents[4] = {"음악","게임","만화","영화"};

    // pContents는 4개의 주소값을 할당받아, 4개의 문자를 요소 값으로 가질 수
    // 있는 포인터 배열이다.
    // 이때, 포인터 배열의 요소는 본질적으로 주소값인데, 이 주소값은
    // 각각의 요소의 첫번째 문자를 가리키고 있다.

    printf("최초포인트:%d\n",point);


    while(1){

        printf("0:종료 1:음악 2:게임 3:만화 4:영화 \n");

        printf("콘텐츠를 구매하시겠습니까?(번호 선택):");

        scanf("%d",&num);

        if(num ==0){

            printf("구매종료");

            break;

        }else{

            if(point<=0){

                printf("포인트가 부족하여 콘텐츠를 구매할 수 없음");

            }else{

                printf("%s 콘텐츠 구매 완료 \n",pContents[num-1]);

                // pContents[0] [1] [2] 의 요소값은 포인터 배열의 본질상 주소값을 가리키는데,
                // 주소 값은 또한 어떠한 값을 가리키고 있으므로 최종적으로 주소가 가리키고 있는
                // 값이 최종값으로 도출된다.

                point = point - 25;

                printf("현재포인트:%d\n",point);

            }

        }

    }

    return 0;
}


