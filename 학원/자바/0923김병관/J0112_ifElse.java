package project001;

import java.util.*;

public class J0112_ifElse {
    public static void main(String[] args) {
    	int budget;
    	int weather;
    	
    	Scanner s = new Scanner(System.in);
    	System.out.print("예산 입력(만원):");
    	budget=s.nextInt();
    	if(budget<200) {
    		System.out.println("국내여행");
    		System.out.print("날씨 입력(1:맑음 2:비옴):");
    		weather=s.nextInt();
    		if(weather==1) {
    			System.out.println("계곡");
    		}else {
    			System.out.println("실내스파");
    		}
    	}else {
    		System.out.println("해외여행");
    	}
    	s.close();
    }
}