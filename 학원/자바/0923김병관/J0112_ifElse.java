package project001;

import java.util.*;

public class J0112_ifElse {
    public static void main(String[] args) {
    	int budget;
    	int weather;
    	
    	Scanner s = new Scanner(System.in);
    	System.out.print("���� �Է�(����):");
    	budget=s.nextInt();
    	if(budget<200) {
    		System.out.println("��������");
    		System.out.print("���� �Է�(1:���� 2:���):");
    		weather=s.nextInt();
    		if(weather==1) {
    			System.out.println("���");
    		}else {
    			System.out.println("�ǳ�����");
    		}
    	}else {
    		System.out.println("�ؿܿ���");
    	}
    	s.close();
    }
}