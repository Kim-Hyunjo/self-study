import sys
from collections import deque

def DFS(graph):
    stack = [V]
    visited = [False for _ in range(N)]
    ans = []
    while stack:
        curNode = stack.pop()
        if not visited[curNode-1]:
            visited[curNode-1] = True
            ans.append(curNode)
            if curNode in graph.keys():
                graph[curNode].sort(reverse=True)
                for node in graph[curNode]:
                    stack.append(node)
    return ans

def BFS(graph):
    queue = deque([V])
    visited = [False for _ in range(N)]
    ans = []
    while queue:
        curNode = queue.popleft()
        if not visited[curNode-1]:
            visited[curNode-1] = True
            ans.append(curNode)
            if curNode in graph.keys():
                graph[curNode].sort()
                for node in graph[curNode]:
                    queue.append(node)
    return ans

N,M,V = map(int, sys.stdin.readline().split())
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

for node in DFS(graph):
    print(node, end=' ')
print()
for node in BFS(graph):
    print(node, end=' ')