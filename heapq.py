import heapq
lst = [(3,5),(4,2),(2,1),(1,4),(3,7),(8,2),(2,0),(2,5)]
heap = []
for x in lst:
    heapq.heappush(heap, x)
    print(heap)
while lst:
    heapq.heappop(heap)
    print(heap)