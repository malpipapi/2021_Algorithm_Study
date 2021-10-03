def solution(n, s, a, b, fares):
    answer = 10e+9
    floyd = []
    INF = 10e+9
    
    for i in range(n+1):
        floyd.append([])
        for j in range(n+1):
            if i==j:
                floyd[i].append(0)
            else:
                floyd[i].append(INF)
                
    for start, to, dis in fares:
        floyd[start][to] = dis
        floyd[to][start] = dis
                
    for k in range(n+1):
        for i in range(n+1):
            for j in range(n+1):
                floyd[i][j] = min(floyd[i][j], floyd[i][k]+floyd[k][j])

    for i in range(1, n+1):
        answer = min(answer, floyd[s][i]+floyd[i][a]+floyd[i][b])
    
    return answer
