#1080 행렬
import sys
N,M = map(int, sys.stdin.readline().split())
A = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(N)]
B = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(N)]
ans = 0
sub = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]  # 현 위치 기준으로 3*3
for i in range(N-2):
    for j in range(M-2):
        if A[i][j] != B[i][j]:  # 현 위치의 값이 A,B에서 서로 다르면 3*3 행렬변환연산
            for k in range(len(sub)):
                y = i+sub[k][0]
                x = j+sub[k][1]
                if  y >= 0 and  x >= 0 and y < N and x < M:
                    B[y][x] = 1 - B[y][x]  # 1 -> 0,  0 -> 1
            ans += 1
for i in range(N):
    for j in range(M):
        if A[i][j] != B[i][j]:
            ans = -1
            break
print(ans)