package com.programmers.level2;

import java.util.Arrays;

public class 77485_uoayop_행렬테두리 {
	public static void main(String[] args) {
		System.out.println(Arrays.toString(solution(6, 6, new int[][] {{2,2,5,4},{3,3,6,6},{5,1,6,3}})));
		// [8, 10, 25]
		System.out.println(Arrays.toString(solution(3, 3, new int[][] {{1,1,2,2},{1,2,2,3},{2,1,3,2},{2,2,3,3}})));
		// [1, 1, 5, 3]
		System.out.println(Arrays.toString(solution(100, 97, new int[][] {{1,1,100,97}})));
		// [1, 1, 5, 3]
		
	}
	
	public static int[][] dir = {{1,0}, {0,1}, {-1,0}, {0,-1}};	// 아래 -> 오른쪽 -> 위 -> 왼쪽
	public static int[] solution(int rows, int columns, int[][] queries) {
		int[][] map = new int[rows+1][columns+1];
		int num = 1;
		for (int i=1; i<=rows; i++) {
			for (int j=1; j<=columns; j++) {
				map[i][j] = num++;
			}
		}

        int[] answer = new int[queries.length];
		for (int i=0; i<queries.length; i++) {
			int[] query = queries[i];
			int x1 = query[0], y1 = query[1], x2 = query[2], y2 = query[3];
			
			int curr_x = x1, curr_y = y1, pre_x = 0, pre_y = 0, idx = 0;
			int start = map[x1][y1];
			int min_value = start;
			while (true) {
				pre_x = curr_x;
				pre_y = curr_y;
				
				curr_x += dir[idx][0];
				curr_y += dir[idx][1];
				
				map[pre_x][pre_y] = map[curr_x][curr_y];
				min_value = Math.min(map[pre_x][pre_y], min_value);
				
				if ((curr_x == x2 && curr_y == y1) || (curr_x == x2 && curr_y == y2) || (curr_x == x1 && curr_y == y2)) idx++;
				
				if (curr_x== x1 && curr_y==y1) {
					map[curr_x][curr_y+1] = start;
					break;
				}
			}
			answer[i] = min_value;
		}
		
//		printmap(map);
        return answer;
    }

	private static void printmap(int[][] map) {
		for (int[] row: map) {
			for (int col: row) {
				System.out.printf("%2d ",col);
			}
			System.out.println();
		}
	}
}
