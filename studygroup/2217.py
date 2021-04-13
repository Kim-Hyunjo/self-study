#2217 로프
import sys

N = int(sys.stdin.readline())
ropes = []
for i in range(N):
    ropes.append(int(sys.stdin.readline()))
ropes.sort()  # 최대중량 기준으로 오름차순 정렬
max_weight = 0
for i in range(len(ropes)):   
    if ropes[i] * (N-i) > max_weight:  # 최소중량 * 이후 로프 개수
        max_weight = ropes[i] * (N-i) 
print(max_weight)