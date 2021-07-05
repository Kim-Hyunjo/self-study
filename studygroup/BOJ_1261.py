# 1261 알고스팟
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
maze = [list(map(int, input().rstrip())) for _ in range(M)]
count = [[-1 for _ in range(N)] for _ in range(M)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
queue = deque()
queue.append((0,0))
count[0][0] = 0
print(queue)

while queue:
    node = queue.popleft()
    x, y = node[0], node[1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if count[ny][nx] == -1:
                if maze[ny][nx] == 0:
                    count[ny][nx] = count[y][x]
                    queue.appendleft((ny, nx))  # 먼저 거치게 하기 위해서
                else:
                    count[ny][nx] = count[y][x] + 1
                    queue.append((ny, nx))
    
    
print(count)
print(count[M-1][N-1])
