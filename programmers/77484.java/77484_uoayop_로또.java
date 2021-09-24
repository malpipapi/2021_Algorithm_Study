package com.programmers.level1;

import java.util.Arrays;
import java.util.HashMap;

public class 77484_uoayop_로또 {
	public static void main(String[] args) {
		System.out.println(Arrays.toString(solution(new int[] {44, 1, 0, 0, 31, 25}, new int[]{31, 10, 45, 1, 6, 19})));
		System.out.println(Arrays.toString(solution(new int[] {0, 0, 0, 0, 0, 0}, new int[]{38, 19, 20, 40, 15, 25})));
		System.out.println(Arrays.toString(solution(new int[] {45, 4, 35, 20, 3, 9}, new int[]{20, 9, 3, 45, 4, 35})));
		System.out.println(Arrays.toString(solution(new int[] {0, 0, 0, 0, 3, 2}, new int[]{1,2,3,4,5,6})));
		System.out.println(Arrays.toString(solution(new int[] {1,2,3,4,5,6}, new int[]{7,8,9,10,11,12})));
	}
	
	public static int[] solution(int[] lottos, int[] win_nums) {
		HashMap<Integer, Integer> count = new HashMap<>();
		
		for (int num: lottos) {
			if (count.containsKey(num)) {
				int cnt = count.get(num);
				count.put(num,cnt+1);
				continue;
			} 
			count.put(num, 1);
		}
		
//		count.forEach((k, v) -> {
//			System.out.println(k+" "+v);
//		});
		
//		0 2
//		1 1
//		25 1
//		44 1
//		31 1

		int wincnt = 0, zerocnt = count.get(0) == null? 0: count.get(0);
		for (int num: win_nums) {
			if (count.containsKey(num)) {
				wincnt++;
			}
		}
		System.out.println(wincnt+" "+zerocnt);
		
        int[] answer = {7-(wincnt+zerocnt) , 7-(wincnt)};
        
        if (wincnt == 0 && zerocnt == 0) {
        	// 0도 없고, 맞는 번호도 없을 때
        	answer[0]--;
        	answer[1]--;
        } else if (wincnt == 0) {
        	// 0은 있지만, 맞는 번호가 없을 때
        	answer[1]--;
        }
        
        return answer;
    }
}
