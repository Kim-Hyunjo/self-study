def solution(s, n):
    answer = ''
    for c in s:
        if c == ' ':
            next_c = ' '
        elif c.islower():
            next_c = chr((ord(c)+n-ord('a'))%26+ord('a'))
        else:
            next_c = chr((ord(c)+n-ord('A'))%26+ord('A'))
        answer += next_c
    return answer