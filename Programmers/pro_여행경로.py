from collections import deque

def BFS(graph, start, used):
    answer = []
    queue = deque([(start, [start], used)])
    while queue:
        cur = queue.popleft()
        cur_airport, cur_lst, cur_used = cur[0], cur[1], cur[2]

        if all(cur_used):
            answer.append(cur_lst)
            continue
        if cur_airport in graph.keys():    
            for node in graph[cur_airport]:
                airport, idx = node[0], node[1]
                if not cur_used[idx]:
                    next_lst = cur_lst[:]
                    next_lst.append(airport)
                    next_used = cur_used[:]
                    next_used[idx] = True
                    queue.append((airport, next_lst, next_used))
    return answer
    
    
def solution(tickets):
    graph = {}  # key: 출발공항, value: (도착공항, 티켓인덱스)
    used = [False for _ in range(len(tickets))]
    
    for i in range(len(tickets)):
        ticket = tickets[i]
        if ticket[0] not in graph.keys():
            graph[ticket[0]] = [(ticket[1], i)]
        else:
            graph[ticket[0]].append((ticket[1], i))
            
    answer = BFS(graph, 'ICN', used)
    answer.sort()
    print(answer[0])
    return answer[0]

solution([["ICN", "COO"], ["ICN", "BOO"], ["COO", "ICN"], ["BOO", "DOO"]])