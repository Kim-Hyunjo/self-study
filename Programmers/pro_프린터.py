from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque()
    for i in range(len(priorities)):
        queue.append((i, priorities[i]))
    
    while queue:
        maxi = max(queue, key=lambda x: x[1])
        doc = queue.popleft()
        print(doc)
        i, p = doc[0], doc[1]
        if p != maxi[1]:
            queue.append(doc)
        else:
            answer += 1
            if i == location:
                break
        
    return answer

print(solution([1, 1, 9, 1, 1, 1], 0))