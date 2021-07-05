import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())
jewels = []
bags = []

for _ in range(N):
    heapq.heappush(jewels, tuple(map(int, input().split())))
for _ in range(K):
    bags.append(int(input().rstrip()))

bags.sort()
answer = 0
candidates = []

for bag in bags:
    while jewels and bag >= jewels[0][0]:
        w, v = heapq.heappop(jewels)
        heapq.heappush(candidates, -v)
    
    if candidates:
        answer -= heapq.heappop(candidates)
    

print(answer)