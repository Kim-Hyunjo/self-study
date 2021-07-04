# 1261 알고스팟
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
maze = [list(map(int, input().rstrip())) for _ in range(N)]
count = [[-1 for _ in range(M)] for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
queue = deque()
queue.append((0,0))
count[0][0] = 0

while queue:
    node = queue.popleft()
    x, y = node[0], node[1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if count[nx][ny] == -1:
                if maze[nx][ny] == 0:
                    count[nx][ny] = count[x][y]
                    queue.appendleft((nx, ny))  # 먼저 거치게 하기 위해서
                else:
                    count[nx][ny] = count[x][y] + 1
                    queue.append((nx, ny))
    print(count)

print(count[N-1][M-1])
