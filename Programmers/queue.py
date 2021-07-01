from collections import deque


queue = deque([(1,3),(2,2),(4,5)])
maxi = max(queue, key=lambda x: x[1])

lst = [2,3]
queue.append(('hi', lst))

while(queue):
    x = queue.popleft()
    if x[0] == 'hi':
        print('!')
        continue
    print(x)
