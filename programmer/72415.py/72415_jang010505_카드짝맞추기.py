from collections import deque
from itertools import permutations
from copy import deepcopy

def control_move(board, start, d):
    now_r, now_c = start
    dr, dc = d
    
    while True:
        nxt_r = now_r + dr
        nxt_c = now_c + dc
        if not (0 <= nxt_r < 4 and 0 <= nxt_c < 4):
            return (now_r, now_c)
        if board[nxt_r][nxt_c] != 0:
            return (nxt_r, nxt_c)
        
        now_r, now_c = nxt_r, nxt_c



def bfs(board, start, end):
    d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    visit = [[-1]*4 for _ in range(4)]
    now_r, now_c = start
    end_r, end_c = end
    dq = deque()
    dq.append([now_r, now_c])
    visit[now_r][now_c] = 0
    
    while dq:
        now_r, now_c = dq.popleft()
        
        if now_r == end_r and now_c == end_c:
            return visit[now_r][now_c]
        
        for dr, dc in d:
            nxt_r = now_r + dr
            nxt_c = now_c + dc
            
            if 0 <= nxt_r < 4 and 0 <= nxt_c < 4 and visit[nxt_r][nxt_c] == -1:
                visit[nxt_r][nxt_c] = visit[now_r][now_c] + 1
                dq.append([nxt_r, nxt_c])
            
            nxt_r, nxt_c = control_move(board, [now_r, now_c], [dr, dc])
            
            if visit[nxt_r][nxt_c] == -1:
                visit[nxt_r][nxt_c] = visit[now_r][now_c] + 1
                dq.append([nxt_r, nxt_c])
            

def solution(board, r, c):
    card_pos = dict()
    
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                if board[i][j] in card_pos:
                    card_pos[board[i][j]].append([i,j])
                else:
                    card_pos[board[i][j]]=[[i,j]]
    
    orders = list(permutations(card_pos.keys(), len(card_pos.keys())))
    answer = 10000
    
    for order in orders:
        now_board = deepcopy(board)
        count = 0
        now_r, now_c = r, c
        
        for now in order:
            left = bfs(now_board, [now_r, now_c], card_pos[now][0])
            right = bfs(now_board, [now_r, now_c], card_pos[now][1])
            
            if left < right:
                count += left
                count += bfs(now_board, card_pos[now][0], card_pos[now][1])
                now_r, now_c = card_pos[now][1]
            else:
                count += right
                count += bfs(now_board, card_pos[now][1], card_pos[now][0])
                now_r, now_c = card_pos[now][0]
            
            now_board[card_pos[now][0][0]][card_pos[now][0][1]] = 0
            now_board[card_pos[now][1][0]][card_pos[now][1][1]] = 0
            count += 2
        
        answer = min(answer, count)
                                           
    return answer
