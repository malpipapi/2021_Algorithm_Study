def solution(new_id):
    new_id = new_id.lower()
    
    temp = ''
    two_lst = ['-', '_', '.']
    
    for x in list(new_id):
        if ord('a') <= ord(x) <= ord('z') or ord('0') <= ord(x) <= ord('9') or x in two_lst:
            temp += x
    
    new_id = temp
    temp = ''
    i = 0
    
    while i < len(new_id):
        while i+1 < len(new_id) and new_id[i] == '.' and new_id[i] == new_id[i+1]:
            i += 1
            
        if i >= len(new_id):
            break
        
        temp += new_id[i]
        i += 1
    
    new_id = temp
    
    if len(new_id) > 0 and new_id[0] == '.':
        new_id = new_id[1:]
    if len(new_id) > 0 and new_id[-1] == '.':
        new_id = new_id[:-1]
    
    if len(new_id) == 0:
        new_id += 'a'

    if len(new_id) > 15:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    
    while len(new_id) < 3:
        new_id += new_id[-1]
    
    return new_id
