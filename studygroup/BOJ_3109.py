# 3109 빵집
import sys
input = sys.stdin.readline

def solution(i, j):
    if j == C-1:
        return True

    for d in dx:
        if 0 <= i+d < R and mapp[i+d][j+1] == "." and not visited[i+d][j+1]:
            visited[i+d][j+1] = True
            if solution(i+d, j+1):
                return True
    return False

R, C = map(int, input().split())
mapp = []
for _ in range(R):
    mapp.append(list(input().rstrip()))
visited = [[False for _ in range(C)] for _ in range(R)]

dx = [-1, 0, 1] 
ans = 0
for i in range(R):
    if mapp[i][0] == '.':
        if solution(i,0):
            ans += 1
print(ans)
