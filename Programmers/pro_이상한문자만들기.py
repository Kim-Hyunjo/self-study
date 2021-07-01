def solution(s):
    answer = ''
    ls = s.split(' ')
    for i in range(len(ls)):
        word = ls[i]
        for j in range(len(word)):
            if j % 2 == 0:
                answer += word[j].upper()
            else:
                answer += word[j].lower()
        if i != len(ls)-1:
            answer += ' '
    return answer