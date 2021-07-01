# https://javaiyagi.tistory.com/586

import sys

N,C = map(int, sys.stdin.readline().split())
M = int(sys.stdin.readline())
delivery = []
available = [C for _ in range(N)] # 각 마을에서 수용가능한 박스 개수

for _ in range(M):
    # [보내는 마을, 받는 마을, 박스 개수] 가 리스트 요소 한 개
    delivery.append(list(map(int, sys.stdin.readline().split())))
delivery = sorted(delivery, key=lambda x:x[1])  # 받는마을 기준으로 오름차순 정렬

ans = 0
for i in range(len(delivery)):
    mini = C + 1
    # 보내는 ~ 받는 사이에 있는 마을 중 수용 가능 개수가 더 적은 곳 있다면
    # 해당 개수로 최솟값(mini) 갱신
    for j in range(delivery[i][0], delivery[i][1]):
        if(available[j] < mini):
            mini = available[j]
    
    # 현재마을에서 실어야할 개수보다 앞으로의 박스 개수 중 최소가 더 작으면,
    # 해당 박스를 실으러 가면 더 이득
    t = min(mini, delivery[i][2])
    ans += t
    # 위의 값을 중간 마을들의 수용가능 개수에서 빼줌
    for j in range(delivery[i][0], delivery[i][1]):
        available[j] -= t

print(ans)