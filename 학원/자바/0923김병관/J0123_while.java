package project001;

public class J0123_while {
    public static void main(String[] args) {
    	int num=0;
    	int s=0;
    	
    	while(true) {
    		num=num+1;
    		s=s+num;
    		if(s>=50) {
    			break;
    		}
    	}
    	System.out.println("1에서"+num+"까지의 합:"+s);
    }
}