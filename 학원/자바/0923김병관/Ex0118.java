package project001;

import java.util.*;

public class Ex0118 {
    public static void main(String[] args) {
    	int dan;
    	
    	Scanner s = new Scanner(System.in);
    	System.out.print("dan input:");
    	dan=s.nextInt();
    	
    	for(int i=1;i<=9;i++) {
    		System.out.println(dan+"*"+i+"="+dan*i);
    	}
    	s.close();
    }
}