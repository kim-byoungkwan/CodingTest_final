#include <stdio.h>
#include <string.h>

main(){

    char juso[30];

    char city[10];

    char gu[10];

    char fulllocation[30]="";

    puts("�ּ� �Է�:");

    gets(juso);

    puts(juso);


    puts("�����Է�:");

    gets(city);

    puts("�� �Է�:");

    gets(gu);

    strcat(fulllocation,city);

    strcat(fulllocation,", ");

    strcat(fulllocation,gu);


    puts(fulllocation);

    return 0;

}

