package project001;

import java.util.*;

public class Ex0119 {
    public static void main(String[] args) {
    	double money;
    	int year;
    	double interest_rate;
    	
    	Scanner s = new Scanner(System.in);
 
    	System.out.print("원금 입력:");
    	money=s.nextDouble();
    	System.out.print("연 입력:");
    	year=s.nextInt();
    	System.out.print("연 이율(%) 입력:");
    	interest_rate=s.nextDouble();
    	
    	for(int i=1;i<=year;i++) {
    		money=money+(money*(interest_rate/100));
    		System.out.println(i+"년 후 금액은:"+money);
    	}
    	System.out.printf("세전 찾을 총 금액:%.0f\n",money);
        s.close();
    }
}