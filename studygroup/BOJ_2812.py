# 2812 크게 만들기
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
num = list(input().rstrip())
answer = []
left = K

for i in range(N):
    while left > 0 and answer and answer[-1] < num[i]:
        answer.pop()
        left -= 1
    answer.append(num[i])

print(int(''.join(answer[:N-K])))


