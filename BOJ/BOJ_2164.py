import collections

N = int(input())
exist = collections.deque()
for i in range(N):
    exist.append(i+1)
for i in range(N-1):
    exist.popleft()
    new = exist.popleft()
    exist.append(new)
print(exist.pop())