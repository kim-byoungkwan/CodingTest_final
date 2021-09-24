package project001;

import java.util.*;

public class Ex0105 {
	public static void main(String[] args) {
		double pi=3.14;
		int r;
		double a;
		
		Scanner s = new Scanner(System.in);
		System.out.print("radius input:");
		r = s.nextInt();
		a= r*r*pi;
		System.out.println("area="+a);
		s.close();
	}
}