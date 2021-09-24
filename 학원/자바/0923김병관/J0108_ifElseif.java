package project001;

import java.util.*;

public class J0108_ifElseif {
	public static void main(String[] args) {
		int a;
		
		Scanner s = new Scanner(System.in);
		System.out.print("score input:");
		a=s.nextInt();
		
		if(a>=90) {
			System.out.println("A grade");
		}else if(a>=80) {
			System.out.println("B grade");
		}else if(a>=70) {
			System.out.println("C grade");
		}else if(a>=60) {
			System.out.println("D grade");
		}else {
			System.out.println("F grade");
		}
		s.close();
	}
}