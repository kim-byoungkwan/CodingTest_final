package project001;

import java.util.*;

public class J0110_random {
	public static void main(String[] args) {
		int a;
		
		Random r = new Random();
		a=r.nextInt(10); //0에서 10미만의 임의의 정수
		System.out.println(a);
	}
}