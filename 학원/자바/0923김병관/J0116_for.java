package project001;

public class J0116_for {
    public static void main(String[] args) {
    	int a_sum=0;
    	int b_sum=0;
    	
    	for(int a=1;a<=2;a++) {
    		System.out.println("AÄÚ½º:"+a+"¹ÙÄû Â°");
    		a_sum=a_sum+1;
    		for(int b=1;b<=3;b++) {
    			System.out.println("    BÄÚ½º:"+b+"¹ÙÄû Â°");
    			b_sum=b_sum+1;
    		}
    	}
    	System.out.println("ÃÑ AÄÚ½º:"+a_sum+"¹ÙÄû");
    	System.out.println("ÃÑ BÄÚ½º:"+b_sum+"¹ÙÄû");
    }
}