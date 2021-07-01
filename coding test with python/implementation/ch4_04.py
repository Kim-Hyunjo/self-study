# [구현] p.118 실전 3 게임 개발

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A, B, d = map(int, input().split())  # d: 0-북, 1-동, 2-남, 3-서
dx = [0,1,0,-1]
dy = [-1,0,1,0]
mapp = []  # 0-육지, 1-바다
for _ in range(N):
    mapp.append(list(int,input().split()))
cnt = 1
mapp[A-1][B-1] = 1

# 북쪽
nA, nB = A, B
for i in range(0,A):
    if mapp[i][B-1] == 0:
        d = 3
        nA += dy[d]
        nB += dx[d]





