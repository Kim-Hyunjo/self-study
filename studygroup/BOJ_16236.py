import sys
from collections import deque

# 아기상어보다 작은 물고기 ==> 지나갈 수 있고, 먹을 수 있다.
# 아기상어와 같은 크기의 물고기 ==> 지나갈 수 있지만, 먹을 수 없다.
# 아기상어보다 큰 물고기 ==> 지나갈 수 없고, 먹을 수 없다.

# 공간내에 아기상어보다 작은 물고기가 없다면 ==> 종료
# 공간내에 아기상어보다 작은 물고기가 있다면
    # 1. 이동 칸 수 가장 적은 물고기
    # 2. 위쪽에 있는 물고기
    # 3. 왼쪽에 있는 물고기
# 의 우선순위로 이동하여 먹음
# 상어의 현재 크기만큼 물고기를 먹으면 상어의 크기 1 증가

# 현재 상어의 위치에서 bfs로 상어보다 작은 물고기 찾음
# (이때 bfs 이동 순서를 위쪽, 왼쪽 순서로)
# (+ 몇 칸 이동했는지 세야함)
# 찾으면 멈추고 상어 위치 바꾼 후 물고기 없애고 상어크기 변화살핌
# 바뀐 위치에서 재탐색
# 탐색끝났다면 종료

def BFS(sx, sy, cnt):
    global mapp
    global shark

    ds = [(0,1),(-1,0),(0,-1),(1,0)]
    queue = deque([(sx,sy)])
    visited = [[False for _ in range(N)] for _ in range(N)]
    times = [[0 for _ in range(N)] for _ in range(N)]
    check = False

    while queue:
        curNode = queue.popleft()
        cx, cy = curNode[0], curNode[1]
        if not visited[cy][cx]:
            visited[cy][cx] = True
            if 0 < mapp[cy][cx] < shark:
                cnt += 1
                check = True
                print(cnt)
                if cnt == shark:
                    cnt = 0
                    shark += 1
                mapp[cy][cx] = 0
                sx, sy = cx, cy
                break
            for d in ds:
                dx = cx + d[0]
                dy = cy + d[1]
                if 0 <= dx < N  and 0 <= dy < N:
                    if not visited[dy][dx]:
                        queue.append((dx,dy))
                        times[dy][dx] = times[cy][cx] + 1
    return check

N = int(sys.stdin.readline())
mapp = []
shark = 2
sx = 0; sy = 0
cnt = 0
for i in range(N):
    mapp.append(list(map(int,sys.stdin.readline().split())))
    for j in range(N):
        if mapp[i][j] == 9:
            sx, sy = j, i

while True:
    if not BFS(sx,sy,cnt):
        break
    time += 


