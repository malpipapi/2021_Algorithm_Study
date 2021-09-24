def solutions(lottos,win):
    answer = []
    changable_num = 0
    answer_num = 0
    for zero in lottos:
        if zero == 0:
            changable_num += 1
    for correct in win:
        for number in lottos:
            if correct == number:
                answer_num += 1
    if answer_num + changable_num == 6:
        answer.append(1)
    elif answer_num + changable_num == 5:
        answer.append(2)
    elif answer_num + changable_num == 4:
        answer.append(3)
    elif answer_num + changable_num == 3:
        answer.append(4)
    elif answer_num + changable_num == 2:
        answer.append(5)
    else:
        answer.append(6)

    if answer_num == 6:
        answer.append(1)
    elif answer_num == 5:
        answer.append(2)
    elif answer_num == 4:
        answer.append(3)
    elif answer_num == 3:
        answer.append(4)
    elif answer_num == 2:
        answer.append(5)
    else:
        answer.append(6)
    
    
    
    return answer

win = [38, 19, 20, 40, 15, 25]
lottos = [0, 0, 0, 0, 0, 0]
print(solutions(lottos,win))