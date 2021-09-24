package project001;

import java.util.*;

public class Ex0111 {
	public static void main(String[] args) {
		int a;
		int b;
		
		Scanner s = new Scanner(System.in);
		System.out.print("number input:");
		a=s.nextInt();
		
		Random r = new Random();
		b=r.nextInt(5)+1;
		System.out.println("Computer:"+b);
		
		if(a==b) {
			System.out.println("¥Á√∑");
		}else {
			System.out.println("≤Œ");
		}
		s.close();
	}
}