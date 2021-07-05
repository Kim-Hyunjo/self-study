import heapq
lst = ['2b', '1a', '3c', '1b', '2a', '3a']
#heapq.heapify(lst)
while lst:
    print(heapq.heappop(lst))