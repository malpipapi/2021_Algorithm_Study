def solution(play_time, adv_time, logs):
    play_time_h, play_time_m, play_time_s = map(int, play_time.split(":"))
    play_time = play_time_h*3600 + play_time_m*60 + play_time_s
    
    adv_time_h, adv_time_m, adv_time_s = map(int, adv_time.split(":"))
    adv_time = adv_time_h*3600 + adv_time_m*60 + adv_time_s
    
    start_logs = list()
    end_logs = list()
    
    for log in logs:
        start, end = log.split('-')
        
        start_h, start_m, start_s = map(int, start.split(":"))
        start = start_h*3600 + start_m*60 + start_s
        start_logs.append(start)
        
        end_h, end_m, end_s = map(int, end.split(":"))
        end = end_h*3600 + end_m*60 + end_s
        end_logs.append(end)
        
    total_time = [0 for i in range(play_time+1)]
    
    for i in range(len(start_logs)):
        total_time[start_logs[i]] += 1
        total_time[end_logs[i]] -= 1
    
    for time in range(1, play_time):
        total_time[time] += total_time[time-1]
    
    for time in range(1, play_time):
        total_time[time] += total_time[time-1]
    
    max_time = -1
    index = 0
    
    for time in range(adv_time - 1, play_time):
        if time >= adv_time:
            if max_time < total_time[time] - total_time[time-adv_time]:
                max_time = total_time[time] - total_time[time-adv_time]
                index = time - adv_time + 1
        else:
            if max_time < total_time[time]:
                max_time = total_time[time]
                index = time - adv_time + 1

    
    answer = ''
    answer += ("%02d"%(index//3600)) + ":"
    index %= 3600
    answer += ("%02d"%(index//60)) + ":"
    index %= 60
    answer += ("%02d"%(index))
    
    
    return answer
