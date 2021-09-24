package project001;

public class J0124_while {
    public static void main(String[] args) {
    	int num=0;
    	int s=0;
    	
    	while(true) {
    		num=num+1;
    		if(num%2==1) {
    			continue;
    		}
    		s=s+num;
    		if(s>=30) {
    			break;
    		}
    	}
    	System.out.println("1에서 "+num+"까지 짝수들의 합:"+s);
    }
}