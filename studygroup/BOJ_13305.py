#13305 주유소
import sys

N = int(sys.stdin.readline())
roads = list(map(int,sys.stdin.readline().split()))  # 도시사이 길의 길이 리스트
prices = list(map(int,sys.stdin.readline().split()))  # 도시의 기름값 리스트
ans = prices[0] * roads[0]  # 첫 주유소는 무조건 이용
min_price = prices[0]
for i in range(1,len(prices)-1):
    # 앞까지의 주유소 중에서 현재 주유소가 가장 저렴하다면 최소 기름값을 갱신하고 현재 주유소에서 주유
    if prices[i] < min_price:  
        ans += prices[i] * roads[i]
        min_price = prices[i]
    else:
        ans += min_price * roads[i]
print(ans)