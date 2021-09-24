package project001;

import java.util.*;

public class J0104_userInput {
    public static void main(String[] args) {
    	int a;
    	String b;
    	
    	Scanner s = new Scanner(System.in);
    	
    	System.out.print("number input:");
    	a = s.nextInt();
    	System.out.println("number="+a);
    	
    	System.out.print("string input:");
    	b=s.next();
    	System.out.println("string="+b);
    	
    	s.close();
    }
}