import sys

E,S,M = map(int, sys.stdin.readline().split())
E %= 15; S %= 28; M %= 19;
i = 0
while True:
    ans = i * 28 + S  # S의 기준에 부합하는 값 중에서
    if ans % 15 == E and ans % 19 == M:  # 다른 두개에 부합하는 것 찾기
        break
    i += 1
if ans == 0:  # 0인 경우는 없으므로 최대값 넣기
    ans = 15 * 28 * 19
print(ans)