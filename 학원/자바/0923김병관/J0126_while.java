package project001;

import java.util.*;

public class J0126_while {
    public static void main(String[] args) {
    	int num1;
    	int num2;
    	int result;
    	String flag="N";
    	
    	Scanner s = new Scanner(System.in);
    	Random r = new Random();
    	
    	do {
    		num1=r.nextInt(10)+1;
    		num2=r.nextInt(10)+1;
    		System.out.print(num1+"*"+num2+"=");
    		result=s.nextInt();
    		if(result==num1*num2) {
    			System.out.println("����");
    		}else {
    			System.out.println("����");
    		}
    		System.out.print("���������� �����Ͻðڽ��ϱ�? Y/N:");
    		flag=s.next();
    	}while(flag.equals("N"));
    	System.out.println("�������� ����");
    	s.close();
    }
}