# [구현] p.110 예제 4-1 상하좌우
import sys
input = sys.stdin.readline

N = int(input())
moves = input().strip().split()
x, y = 1, 1

for move in moves:
    xx = x; yy = y
    if move == 'L':
        xx -= 1
    elif move == 'R':
        xx += 1
    elif move == 'U':
        yy -= 1
    elif move == 'D':
        yy += 1
    if 1 <= xx <= N and 1 <= yy <= N:
        x, y = xx, yy

print(y,x,end=' ')
        

