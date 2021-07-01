class Node:
    def __init__(self, num, distance):
        self.num = num
        self.distance = distance

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
answer = []
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

start_node = Node(X, 0)
queue = [start_node]
visited = [False for _ in range(N+1)]
while queue:
    now = queue.pop(0)
    next = graph[now.num]
    if now.distance < K - 1:
        for n in next:
            if visited[n]:
                continue
            else:
                visited[n] = True
                new_node = Node(n, now.distance+1)
                queue.append(new_node)
    else:
        for n in next:
            if not visited[n]:
                answer.append(n)
        break

if not answer:
    print(-1)
else:
    answer = sorted(answer)
    for a in answer:
        print(a)