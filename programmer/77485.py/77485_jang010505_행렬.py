def solution(rows, columns, queries):
    answer = []

    map_info = [[i*columns+j for j in range(1, columns+1)]
                for i in range(rows)]

    for x1, y1, x2, y2 in queries:
        min_value = rows*columns

        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1

        temp = map_info[x1][y1]
        min_value = min(temp, min_value)

        for dy in range(y1+1, y2+1):
            temp, map_info[x1][dy] = map_info[x1][dy], temp
            min_value = min(temp, min_value)
        
        for dx in range(x1+1, x2+1):
            temp, map_info[dx][y2] = map_info[dx][y2], temp
            min_value = min(temp, min_value)

        for dy in range(y2-1, y1-1, -1):
            temp, map_info[x2][dy] = map_info[x2][dy], temp
            min_value = min(temp, min_value)

        for dx in range(x2-1, x1-1, -1):
            temp, map_info[dx][y1] = map_info[dx][y1], temp
            min_value = min(temp, min_value)
        
        answer.append(min_value)

    return answer
