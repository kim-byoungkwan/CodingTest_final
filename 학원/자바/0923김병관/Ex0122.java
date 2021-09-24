package project001;

import java.util.*;

public class Ex0122 {
    public static void main(String[] args) {
    	int num;
    	int s23=0;
    	
    	Scanner s = new Scanner(System.in);
    	System.out.print("????:");
    	num=s.nextInt();
    	
    	while(num>0) {
    		if(num%2==0 || num%3==0) {
    			s23=s23+num;
    		}
    		num=num-1;
    	}
    	System.out.println(s23);
    	s.close();
    }
}