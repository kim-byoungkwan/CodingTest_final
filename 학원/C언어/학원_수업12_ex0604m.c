#include <stdio.h>

main(){

    int num;

    int tot;


    printf("�����Է�:");

    scanf(" %d",&num);

    tot = f_sum(num);

    printf("����:%d",tot);

    return 0;

}


f_sum(int num){

    int i;

    int tot=0;

    for(i=1;i<=num;i++){

        tot = tot +i;

    }

    return tot;

}

// f_sum �� ���� �Լ��� ���ǰ������� ���� �ڷ����� ���� ������ ���� �Լ��� ��Ŀ������ ǥ���� ������
// ���� �������� ������ �ǹ����� �ʴ´�.
// ����, ���� ���� ���� ����Ͽ� ���� ���� ����ϴ� main() �Լ������� ������ f_sum �Լ��� �μ���
// �����ؾ߸� f_sum �Լ� ��Ŀ������ �̿��Ͽ� ���� ���� ������ �� �ִ�.
