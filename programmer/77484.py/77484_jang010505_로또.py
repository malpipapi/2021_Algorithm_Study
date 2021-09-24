def solution(lottos, win_nums):
    # 효율을 위해 집합으로 재정의
    win_nums = set(win_nums) 
    
    '''
    win_count : 알 수 없는 상테에서 당첨된 횟수
    zero_count : 알 수 없는 번호의 수
    '''
    win_count = 0
    zero_count = 0 
    
    for number in lottos:
        if number == 0:
            zero_count += 1
        elif number in win_nums:
            win_count += 1
        
    
    '''
    최대 순위 : 7 - max(zero_count + win_count, 1)
    최소 순위 : 7 - max(win_count, 1)
    '''
    
    answer = [7-max(zero_count+win_count, 1), 7-max(win_count, 1)]
    
    return answer
