def solution(n, results):
    answer = 0
    graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for result in results:
        win, lose = result[0], result[1]
        graph[win][lose] = 1
        graph[lose][win] = -1

    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range(1, n+1):
                if graph[i][j] == 0:
                    if graph[i][k] == 1 and graph[k][j] == 1:
                        graph[i][j] = 1
                        graph[j][i] = -1
                    if graph[i][k] == -1 and graph[k][j] == -1:
                        graph[i][j] = -1
                        graph[j][i] = 1
    
    for lst in graph:
        if lst.count(0) == 2:
            answer += 1
    return answer

print(solution(5,	[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))