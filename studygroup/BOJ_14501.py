from sys import stdin

N = int(stdin.readline().strip())
c = []
dp = [0 for _ in range(N+1)] # idx일 만큼 일했을 때 최대보수
for _ in range(N):
    c.append(list(map(int,stdin.readline().split())))

for i in range(N-1,-1,-1):
    if c[i][0] + i <= N: # 날짜 초과안함
        dp[i] = max(c[i][1]+dp[i+c[i][0]], dp[i+1])
    else: # 날짜 초과함
        dp[i] = dp[i+1]

print(dp[0])

