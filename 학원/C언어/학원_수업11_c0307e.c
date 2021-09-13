#include <stdio.h>
#include <string.h>

main(){

    char juso[30];

    char city[10];

    char gu[10];

    char fulllocation[30]="";

    puts("주소 입력:");

    gets(juso);

    puts(juso);


    puts("도시입력:");

    gets(city);

    puts("구 입력:");

    gets(gu);

    strcat(fulllocation,city);

    strcat(fulllocation,", ");

    strcat(fulllocation,gu);


    puts(fulllocation);

    return 0;

}

