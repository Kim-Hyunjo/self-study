# [구현] p.115 실전 2 왕실의 나이트

import sys
input = sys.stdin.readline

def check(x, y, size):
    return 1 <= x <= size and 1 <= y <= size

loca = input()
x, y = ord(loca[0])-ord('a')+1, int(loca[1])
SIZE = 8
cnt = 0

d1 = [2,-2]
d2 = [1,-1]

for a in d1:
    for b in d2:
        nx = x + a
        ny = y + b
        if check(nx,ny,SIZE):
            cnt += 1
        if check(ny,nx,SIZE):
            cnt += 1

print(cnt)

