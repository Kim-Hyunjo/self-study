import sys

def getDistanceInClockwise(dirr, dis):  # 원점(0,0)에서 시계방향으로 동근 또는 매장까지의 거리
    if dirr == 1:
        return dis
    elif dirr == 2:
        return 2*N + M - dis
    elif dirr == 3:
        return 2*N + 2*M - dis
    else:
        return N + dis

def getDistanceFromDong(store, dong):  # 동근으로부터 매장까지의 거리(시계, 반시계 방향 중 최소)
    distance = abs(dong - store)
    return min(distance, (N+M)*2 - distance)

N,M = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
stores = []

for _ in range(K):
    s_dir, s_dis = map(int, sys.stdin.readline().split())
    stores.append(getDistanceInClockwise(s_dir, s_dis))
x_dir, x_dis = map(int, sys.stdin.readline().split())
dong = getDistanceInClockwise(x_dir, x_dis)
      
ans = 0
for store in stores:
    ans += getDistanceFromDong(store, dong)

print(ans)