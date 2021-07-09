# 1374 강의실
import sys
import heapq

input = sys.stdin.readline

N = int(input().rstrip())
lectures = []
classes = []
for _ in range(N):
    lectures.append(tuple(map(int, input().split())))

lectures.sort(key=lambda x: x[1])
heapq.heappush(classes, lectures[0][2])
for lecture in lectures[1:]:
    s, e = lecture[1], lecture[2]
    if classes[0] > s:
        heapq.heappush(classes, e)
    else:
        heapq.heappop(classes)
        heapq.heappush(classes, e)

print(len(classes))

    
    