from sys import stdin
from math import pow

N = int(stdin.readline().strip())
maxis = [-int(pow(10,9))-1 for _ in range(N)]
for _ in range(N):
    nums = list(map(int,stdin.readline().strip().split()))
    nums.extend(maxis)
    nums.sort(reverse=True)
    maxis = nums[:N]
print(maxis[-1])