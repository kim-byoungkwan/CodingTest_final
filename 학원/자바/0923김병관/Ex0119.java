package project001;

import java.util.*;

public class Ex0119 {
    public static void main(String[] args) {
    	double money;
    	int year;
    	double interest_rate;
    	
    	Scanner s = new Scanner(System.in);
 
    	System.out.print("���� �Է�:");
    	money=s.nextDouble();
    	System.out.print("�� �Է�:");
    	year=s.nextInt();
    	System.out.print("�� ����(%) �Է�:");
    	interest_rate=s.nextDouble();
    	
    	for(int i=1;i<=year;i++) {
    		money=money+(money*(interest_rate/100));
    		System.out.println(i+"�� �� �ݾ���:"+money);
    	}
    	System.out.printf("���� ã�� �� �ݾ�:%.0f\n",money);
        s.close();
    }
}