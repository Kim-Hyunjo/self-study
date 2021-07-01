from sys import stdin

N = int(stdin.readline().strip())
meets = []
for _ in range(N):
    s,e = map(int,stdin.readline().strip().split())
    meets.append((s,e))

meets.sort(key=lambda x: (x[1],x[0]))
start,end = meets[0][0], meets[0][1]
cnt = 1
for meet in meets[1:]:
    if meet[0] >= end:
        start = meet[0]
        end = meet[1]
        cnt += 1
print(cnt)

