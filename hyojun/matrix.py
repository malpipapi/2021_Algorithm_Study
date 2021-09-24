#행렬 만들기
#array = [[0 for col in range(columns)] for row in range(rows)]
def solution(rows,colums,queries):
    answer = []
    matrix = []
    row_num = 6
    col_num = 6
    cnt = 1
    for row in range(row_num):
        matrix.append([])
        for col in range(col_num):
            matrix[row].append(cnt)
            cnt += 1

    for x1,y1,x2,y2 in queries:
        tmp = matrix[x1-1][y1-1] #한칸 씩 밀린 행렬 표기법에 -1
        mini = tmp               #temp가 matrix[x1-1][y1-1]인 이유
                                 #행렬이 다 돌고 나면 마지막으로 남는 부분이기 떄문에
        #왼쪽 세로부터 행렬 옮겨주기
        for k in range(x1-1,x2-1): #x1 = 2 x2 = 5
            test =matrix[k+1][y1-1] #y1 = 2
            matrix[k][y1-1]= test
            mini = min(mini,test)
        #하단 가로
        for k in range(y1-1,y2-1):
            test = matrix[x2-1][k+1]
            matrix[x2-1][k] = test
            mini = min(mini,test)
        
        #왼쪽 세로
        for k in range(x2-1,x1-1,-1):
            test = matrix[k-1][y2-1]
            matrix[k][y2-1] = test
            mini = min(mini,test)
        
        #상단 가로
        for k in range(y2-1,y1-1,-1):
            test = matrix[x1-1][k-1]
            matrix[x1-1][k] = test
            mini = min(mini,test)

        matrix[x1-1][y1] = tmp
        answer.append(mini)
    
    return answer
# 1  2  3  4  5  6 
# 7  8  9  10 11 12 
# 13 14 15 16 17 18 
# 19 20 21 22 23 24 
# 25 26 27 28 29 30 
# 31 32 33 34 35 36                             





#행렬 print
# for row in range(row_num):
#     for col in range(col_num):
#         print(matrix[row][col],end = ' ')
#     print()
#(x1,y1) (x2-1,y2-1)만큼의 직사각형이 만들어짐