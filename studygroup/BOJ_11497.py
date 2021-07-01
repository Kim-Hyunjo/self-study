from sys import stdin

T = int(stdin.readline().strip())
for t in range(T):
    N = int(stdin.readline().strip())
    logs = list(map(int,stdin.readline().strip().split()))
    logs.sort()
    maxi = logs[1] - logs[0]
    for i in range(len(logs) - 3):
        maxi = max(maxi, logs[i+2] - logs[i], logs[i+3] - logs[i+1])
    print(maxi)

