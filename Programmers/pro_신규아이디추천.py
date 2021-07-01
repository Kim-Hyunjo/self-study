import re

def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub('[^0-9a-zA-Zㄱ-힗-_.]', '', new_id)
    temp = ''
    for i in range(len(new_id)):
        if new_id[i] != '.':
            temp += new_id[i]
        else:          
            if i != len(new_id)-1:
                if new_id[i+1] != '.':
                    temp += '.'
    new_id = temp[:]  
    if new_id == '.':
        new_id = ''
    else:
        if new_id != '' and new_id[0] == '.':
            new_id = new_id[1:]
        if new_id != '' and new_id[-1] == '.':
            new_id = new_id[:-1]
    if new_id == '':
        new_id = 'a'
    if len(new_id) >= 16:
        new_id = new_id[:15]
        while new_id != '' and new_id[-1] == '.':
            new_id = new_id[:-1]
    while len(new_id) <= 2:
        new_id += new_id[-1]
    answer = new_id
    return answer