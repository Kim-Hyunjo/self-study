import sys
input = sys.stdin.readline

str1 = input().strip()
str2 = input().strip()

dp = [["" for _ in range(len(str2)+1)] for _ in range(len(str1)+1)]

for i in range(1,len(str1)+1):
    for j in range(1,len(str2)+1):
        if str1[i-1] == str2[j-1]: # 새로 확인한 char이 같으면 추가
            dp[i][j] = dp[i-1][j-1] + str1[i-1]
        else: # 다르면 위나 옆중에 최장
            dp[i][j] = max(dp[i][j-1], dp[i-1][j], key=lambda x: len(x))

print(len(dp[-1][-1]))
print(dp[-1][-1])
print(dp)
            