#include <stdio.h>

changesome(int i,float * newX,int iArr[5]);

// �� ó�� ������ ȣ���� �Լ��� ���Ͽ� �̸� ǥ���س��� ���� �Լ� �����̶�� �Ѵ�.

main(){

    int i = 10;

    int ctr;

    float x = 20.2;

    int iArr[5]={10,20,30,40,50};


    printf("�Լ��� ȣ���ϱ� ���� ������:\n");

    printf("i = %d\n",i);

    printf("x=%.1f\n",x);

    for(ctr = 0;ctr<5;ctr++){

        printf("iArr[%d] = %d\n",ctr,iArr[ctr]);

    }

    // ���� iArr[] �迭�� ��Ұ��� ������ ��Ұ����� ��µǰ� �ȴ�.

    changesome(i,&x,iArr);

    printf("�Լ��� ȣ���� ���� ������:\n");

    printf("i=%d\n",i);

    printf("x=%.if\n",x);

    for(ctr=0;ctr<5;ctr++){

        printf("iArr[%d]=%d\n",ctr,iArr[ctr]);

        // �̶��� iArr[]�� ��Ұ��� ���� changesome �Լ��� ����� ���� ��� ���� ���� ������
        // ���� ���̹Ƿ�, ���ʿ� ���ǵ� ��Ұ��� �ٸ���.

    }

    return 0;

}

changesome(int i,float * newX,int iArr[5]){

    int j;

    i = 11;

    *newX=30.3;

    // chagnesome �Լ��� ������ �� �μ����� �̹� newX ������ ������ ������ ���ǵǾ����Ƿ�,
    // *ǥ�� ���� newX ������ �̹� �ּҰ��� ǥ���ϴµ�, ������ *�� �ٿ��� ǥ���Ͽ����Ƿ�,
    // newX �� ����Ű�� �ּҿ� �����Ǵ� ���� �ǹ��ϰ�, �� ���� 30.3�� �Ҵ�Ǿ����Ƿ�, ���������
    // changesome �Լ��� �ι�° �μ��� �׻� 30.3 ���� ���� ���� �������Եȴ�.

    for(j=0;j<5;j++){

        iArr[j] = 1+10*j;

    }

    return;

}

