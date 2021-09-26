def solution(enroll, referral, seller, amount):
    answer = [0 for i in range(len(enroll)+1)]
    enroll.insert(0, "center")
    name_oder = {name: idx for idx, name in enumerate(enroll)}
    parents = [-1 for i in range(len(enroll)+1)]

    for idx, name in enumerate(referral):
        if name == '-':
            parents[idx+1] = 0
        else:
            parents[idx+1] = name_oder[name]

    for name, count in zip(seller, amount):
        temp = name_oder[name]
        profit = count*100
        distribution = profit//10

        while temp != -1 and profit != 0:
            answer[temp] += profit - distribution
            profit = distribution
            distribution = profit//10
            temp = parents[temp]

    return answer[1:]
