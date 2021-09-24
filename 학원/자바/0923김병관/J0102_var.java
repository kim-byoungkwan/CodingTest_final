package project001;

public class J0102_var {
	public static void main(String[] args) {
		int a=6;
		int b=4;
		
		a=a+1;
		System.out.println(a);
		System.out.println(a+b);
		System.out.println(a-b);
		System.out.println(a*b);
		System.out.println(a/b);
		System.out.println(a%b);
		b=b-1;
		System.out.println((float)a/(float)b);
		System.out.printf("%.2f\n",(float)a/(float)b);
	}
}