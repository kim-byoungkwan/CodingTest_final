package project001;

public class J0116_for {
    public static void main(String[] args) {
    	int a_sum=0;
    	int b_sum=0;
    	
    	for(int a=1;a<=2;a++) {
    		System.out.println("A�ڽ�:"+a+"���� °");
    		a_sum=a_sum+1;
    		for(int b=1;b<=3;b++) {
    			System.out.println("    B�ڽ�:"+b+"���� °");
    			b_sum=b_sum+1;
    		}
    	}
    	System.out.println("�� A�ڽ�:"+a_sum+"����");
    	System.out.println("�� B�ڽ�:"+b_sum+"����");
    }
}