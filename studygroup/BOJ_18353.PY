from sys import stdin

n = int(stdin.readline().strip())
sols = list(map(int,stdin.readline().split()))

ans = [1 for _ in range(n)]

for i in range(n):
    for j in range(len(sols[:i])):
        if sols[i] < sols[j] and ans[i] < ans[j] + 1:
            ans[i] = ans[j] + 1

print(n - max(ans))