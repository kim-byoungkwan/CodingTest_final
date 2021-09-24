package project001;

import java.util.*;

public class J0107_ifElse {
	public static void main(String[] args) {
		int a;
		
		Scanner s = new Scanner(System.in);
		System.out.print("number input:");
		a=s.nextInt();
		
		if(a%2==0) {
			System.out.println("even");
		}else {
			System.out.println("odd");
		}
		s.close();
	}
}