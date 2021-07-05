import sys
input = sys.stdin.readline

N, K = map(int, input().split())
jewels = []
bags = []
check = [False] * K
for _ in range(N):
    m, v = map(int, input().split())
    jewels.append((m, v))
for _ in range(K):
    bags.append(int(input().rstrip()))

answer = 0
jewels.sort(key=lambda x: x[1], reverse=True)
bags.sort()

for jewel in jewels:
    w, v = jewel[0], jewel[1]
    if w > bags[-1]:
        continue
    start, end = 0, K-1
    while start <= end:
        mid = (start + end) // 2 
        if (end - start) == 1 and bags[start] <= w < bags[end] and not check[start]:
            answer += v
            check[start] = True
            break
        elif w < bags[mid]:
            end = mid
        elif w >= bags[mid]:
            start = mid
        print(start, end, end=' ')

print(answer)