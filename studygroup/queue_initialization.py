from collections import deque

queue_1 = deque((1,2))
queue_2 = deque([(1,2),(3,4)])
print(queue_1.popleft())
print(queue_2.popleft())


