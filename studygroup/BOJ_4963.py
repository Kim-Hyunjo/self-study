import sys
from collections import deque

def BFS(i,j):
    global visited  # 방문 여부 전역으로
    dxs = [-1,0,1]
    dys = [-1,0,1]
    queue = deque([(i,j)])
    while queue:
        curNode = queue.popleft()
        x,y = curNode[0], curNode[1]
        if not visited[y][x]:
            visited[y][x] = True
            for dx in dxs:
                for dy in dys:
                    xx = x+dx; yy = y+dy
                    if 0 <= xx < w  and 0 <= yy < h:
                        if not visited[yy][xx] and mapp[yy][xx] == 1:
                            queue.append((xx,yy))
        

while True:
    w,h = map(int, sys.stdin.readline().split())
    ans = 0
    if w == 0 and h == 0:
        break
    mapp = []
    for _ in range(h):
        mapp.append(list(map(int, sys.stdin.readline().split())))
    visited = [[False for _ in range(w+1)] for _ in range(h+1)]
    for i in range(w):
        for j in range(h):
            if mapp[j][i] == 1 and not visited[j][i]:
                BFS(i,j)
                ans += 1
    print(ans)