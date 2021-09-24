package com.programmers.level3;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;

public class 77486_uoayop_다단계칫솔 {
	public static void main(String[] args) {
		System.out.println(Arrays.toString(solution(
				new String[] {"john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"}, 
				new String[] {"-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"}, 
				new String[] {"young", "john", "tod", "emily", "mary"},
				new int[] {12, 4, 2, 5, 10})));
		// [360, 958, 108, 0, 450, 18, 180, 1080]
		
		System.out.println(Arrays.toString(solution(
				new String[] {"john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"}, 
				new String[] {"-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"}, 
				new String[] {"sam", "emily", "jaimie", "edward"},
				new int[] {2, 3, 5, 4})));
		// [0, 110, 378, 180, 270, 450, 0, 0]
	}
	
	public static class user{
		String name;
		String boss;
		ArrayList<user> emp;
		int sell = 0;
		
		public user(String name, String boss) {
			emp = new ArrayList<>();
			this.name = name;
			this.boss = boss;
		}
		
		public void addEmp(user u) {
			emp.add(u);
		}
		
		public void addSell(int sell) {
			this.sell += sell;
		}

		@Override
		public String toString() {
			return "user [name=" + name + ", boss=" + boss + ", emp=" + emp + ", sell=" + sell + "]";
		}
	}
	
	public static HashMap<String, user> map = new HashMap<>();
	
	public static int[] solution(String[] enroll, String[] referral, String[] seller, int[] amount) {
        int[] answer = new int[enroll.length];
        
        map.put("-", new user("-", null));
        for (int i=0; i<enroll.length; i++) {
        	map.put(enroll[i], new user(enroll[i], referral[i]));
        }

        for (int i=0; i<referral.length; i++) {
        	user boss = map.get(referral[i]);
        	boss.addEmp(map.get(enroll[i]));
        	map.put(referral[i], boss);
        }
        
        for (int i=0; i<seller.length; i++) {
        	user curr = map.get(seller[i]);
        	int sell = amount[i] * 100;
        	int curr_sell = (int)(sell * 0.9);
        	int to_boss = (int)(sell * 0.1);
        	
        	curr.addSell(curr_sell);
        	
        	String boss_name = curr.boss;
        	while (boss_name != null && to_boss > 0) {
        		user boss = map.get(boss_name);
        		if (to_boss < 10) { boss.addSell(to_boss); break; }
        		else {
        			int boss_sell = (int) Math.ceil(to_boss * 0.9);
        		
	        		boss.addSell(boss_sell);
	
	        		to_boss = to_boss - boss_sell;
	        		boss_name = boss.boss;
	        	}
        	}
        }
        
        for (int i=0; i<enroll.length; i++) {
        	answer[i] = map.get(enroll[i]).sell;
        }
        return answer;
    }
}
