package project001;

import java.util.*;

public class J0125_while {
    public static void main(String[] args) {
    	int num;
    	int count=0;
    	int sum=0;
    	
    	Scanner s = new Scanner(System.in);
    	
    	while(true) {
    		System.out.print("���� �Է�(0:������,1~9:���� ����):");
    		num=s.nextInt();
    		if(num==0) {
    			break;
    		}
    		sum=sum+num;
    		count=count+1;
    	}
    	System.out.println(count+"�� ���� ��:"+sum);
    	s.close();
    }
}