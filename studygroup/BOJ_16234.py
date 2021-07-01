import sys
from collections import deque

# 1. 국경 전체 오픈
# 2. bfs로 국경 오픈된 나라끼리 묶어 인구수 계산하고 방문하지 않은 곳 중에 더이상 오픈할 곳이 없으면 종료
# 3. 더이상 인구이동 없을때까지 1-2 반복

def BFS(x,y):
    global check
    visited = [(x,y)]
    queue = deque([(x,y)])
    pop_sum = 0
    cnt = 0

    while queue:
        x,y = queue.popleft()
        check[y][x] = True
        pop_sum += A[y][x]
        cnt += 1
        dirr = [(-1,0),(1,0),(0,-1),(0,1)]

        for d in dirr:
            xx = x + d[0]
            yy = y + d[1]
            if xx >= 0 and yy >= 0 and xx < N and yy < N:
                if (xx, yy)  not in visited and open(A[y][x],A[yy][xx]):
                    check[yy][xx] = True
                    

                    

def open(a,b):
    return abs(a-b) >= L and abs(a-b) <= R

N,L,R = map(int, sys.stdin.readline().split())
A = []
check = [[False for _ in range(N)] for _ in range(N)]
for _ in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))

while True:
    for i in range(N):
        for j in range(N):
            BFS(i,j)
