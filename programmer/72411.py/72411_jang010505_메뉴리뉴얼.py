from itertools import combinations

def solution(orders, course):
    
    menu_set = set()
    course_dict = dict()
    max_len = [2 for i in range(max(course)+1)]
    max_str = [[] for i in range(max(course)+1)]
    
    for order in orders:
        for number in course:
            for com in combinations(order, number):
                com = sorted(com)
                com = "".join(com)
                
                if com in course_dict:
                    course_dict[com] += 1
                else:
                    course_dict[com] = 1

    for key, value in course_dict.items():
        if max_len[len(key)] < value:
            max_len[len(key)] = value
            max_str[len(key)] = [key]
        elif max_len[len(key)] == value:
            max_str[len(key)].append(key)

    answer = sorted(sum(max_str, []))
    
    return answer
