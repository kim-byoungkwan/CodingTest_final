package project001;

import java.util.*;

public class Ex0109 {
	public static void main(String[] args) {
		int a;
		int b;
		
		Scanner s = new Scanner(System.in);
		System.out.print("number1 input:");
		a=s.nextInt();
		System.out.print("number2 input:");
		b=s.nextInt();
		
		if(a-b==1 || b-a==1) {
			System.out.print("sequence");
		}else {
			System.out.print("Not sequence");
		}
		s.close();
	}
}