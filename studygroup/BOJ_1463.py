from sys import stdin

N = int(stdin.readline().strip())
dp = [0,0,1,1] # 각 인덱스가 X일 경우 연산횟수

for i in range(4,N): # 인덱스 4부터 구함
    dp.append(dp[i-1]+1) # 3번 연산으로 가능한 연산횟수
    # 기존 연산 횟수와 1,2 번 연산으로 가능한 연산횟수 비교
    if i % 2 == 0:
        dp[i] = min(dp[i//2]+1, dp[i])
    if i % 3 == 0:
        dp[i] = min(dp[i//3]+1, dp[i])

print(dp[N])


