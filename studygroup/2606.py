import sys

def count_infected(graph):
    cnt = 0
    stack = [1]
    visited = [False for _ in range(N)]
    while stack:
        curNode = stack.pop()
        if not visited[curNode-1]:
            visited[curNode-1] = True
            cnt += 1
            for node in graph[curNode]:
                stack.append(node)
    return cnt-1

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = {}
for _ in range(M):
    A,B = map(int, sys.stdin.readline().split())
    if A not in graph.keys():
        graph[A] = [B]
    else:
        graph[A].append(B)
    if B not in graph.keys():
        graph[B] = [A]
    else:
        graph[B].append(A)

print(count_infected(graph))