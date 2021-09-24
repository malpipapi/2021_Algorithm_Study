#자신의 조직에 이익의 10%를 분배해주고 자신은 90%의 이익을 받는다.
#자신이 조직에 추천시켜 가입시킨 판매원이 판매한 이익의 10%도 받게 된다.
#원 단위는 절사한다.10%를 계산한 금액이 1원 미만인 경우 이득분배x
#판매원의 이름을 담은 배열 = enroll
#다단계 조직에 참여시킨 다른 판매원의 이름을 담은 배열 = referral
#판매량 집계 데이터의 판매원 이름을 나열한 배열=seller
#판매량 집계 데이터의 판매 수량을 나열한 배열 amount
#referral이 -인 경우 center에게 수당이 나가는 걸로 계산 
#단 answer에 들어가지는 않는다.


#트리문제
def solution(enroll, referral, seller, amount):
    answer = []
    dicts = {}
    tree_dicts = {}
    for i in range(len(enroll)):
        tree_dicts[enroll[i]] = referral[i]
        dicts[enroll[i]] = 0
    
    for i in range(len(seller)):
        cost = amount[i]*100
        node = seller[i]
        while node != '-':
            parent = tree_dicts[node]
            if cost*0.1 <1:
                dicts[node] += cost
                break
            dicts[node] += (cost-(cost//10))
            cost //= 10
            node = parent
        
    for name in enroll:
        answer.append(int(dicts[name]))
    return answer