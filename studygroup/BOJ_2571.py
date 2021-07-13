# 2571 색종이 - 3
import sys
input = sys.stdin.readline

N = int(input().rstrip())
papers = []
mapp = [[0 for _ in range(100)] for _ in range(100)]
for _ in range(N):
    x, y = map(int, input().split())
    for i in range(y+10):
        for j in range(x+10):
            mapp[i][j] = 1



