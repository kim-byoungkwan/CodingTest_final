#include <stdio.h>

// scanf�� ��� ������ �ּҰ����� ���� �Ҵ� �޾� �� ��� ������ ����
// �Ҵ��ϴ� �����̹Ƿ�, ���������� scanf�� �Ҵ���� �ּҰ����� �ش��ϴ�
// ������ �̸� �����ؾ��Ѵ�.

main(){

int card;

printf("����ī�� ��ȣ �Է�:");

scanf("%d",&card);

if(card <= 13){

    printf("�����̵�");

}else if(card <= 26){

    printf("���̾Ƹ��");

}else if(card <= 39){

    printf("��Ʈ");

}else if(card <= 52){

    printf("Ŭ�ι�");

}else{

    printf("����");

}

return 0;

}


