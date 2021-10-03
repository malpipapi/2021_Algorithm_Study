def solution(info, query):
    
    answer = []
    language_dict = {"cpp":0, "java":1, "python":2, "-":3}
    job_dict = {"backend":0, "frontend":1, "-":2}
    career_dict = {"junior":0, "senior":1, "-":2}
    food_dict = {"chicken":0, "pizza":1, "-":2}
    
    group = []
    
    for i in range(4):
        group.append([])
        for j in range(3):
            group[i].append([])
            for k in range(3):
                group[i][j].append([])
                for l in range(3):
                    group[i][j][k].append([])
    
    for temp in info:
        language, job, career, food, grade = temp.split()
        
        languages = [language_dict[language], 3]
        jobs = [job_dict[job], 2]
        careers = [career_dict[career], 2]
        foods = [food_dict[food], 2]
        grade = int(grade)
        
        for language in languages:
            for job in jobs:
                for career in careers:
                    for food in foods:
                        group[language][job][career][food].append(grade)
    
    for i in range(4):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    group[i][j][k][l].sort()
        
    for string in query:
        language, temp1, job, temp2, career, temp3, food, grade = string.split()
        language = language_dict[language]
        job = job_dict[job]
        career = career_dict[career]
        food = food_dict[food]
        grade = int(grade)
        n = len(group[language][job][career][food])
        left = 0
        right = n
        
        while left < right:
            mid = (left+right)//2
            if group[language][job][career][food][mid] >= grade:
                right = mid
            else:
                left = mid+1
        
        answer.append(n-right)
        
    return answer
