import sys
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    a,b = map(int,input().split())
    lst.append((a,b))

lst.sort(key=lambda x: x[0])

leng = [0 for _ in range(N)]
for i in range(N):
    leng[i] = 1
    for j in range(i):
        if lst[j][1] < lst[i][1]:
            leng[i] = max(leng[i], leng[j]+1)
print(N - max(leng))