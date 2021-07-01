from sys import stdin
import heapq  # 최소 힙: 최소값이 인덱스 0이자 루트

N = int(stdin.readline().strip())
times = []
for _ in range(N):
    S,T = map(int, stdin.readline().strip().split())
    times.append((S,T))

classes = []  # 강의실 별 끝나는 시간 저장
#  시작 시간 기준으로 정렬
times.sort(key=lambda x: x[0])

for time in times:
    # 이미 있는 수업의 끝시간 중 가장 빠른것보다 보다 현 수업의 시작시간이 늦을때
    if classes and classes[0] <= time[0]:
        heapq.heappop(classes)  # 가장 작은 원소 삭제
    heapq.heappush(classes,time[1])  # 현 수업 끝시간 저장

print(len(classes))