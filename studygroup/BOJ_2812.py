# 2812 크게 만들기
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
num = list(input().rstrip())
answer = []

removed = 0
left = K
while removed < K:
    n = max(num[:left+1])
    n_idx = num.index(n)
    removed += n_idx
    for _ in range(n_idx):
        num.pop(0)
    answer.append(num.pop(0))
    left -= n_idx
    print(num)
    print(answer)
    print(removed)
    print(left)

print(int(''.join(answer+num)))


