#15829 Hashing
import sys
r =31; M = 1234567891;
L = int(input())
line = sys.stdin.readline()
ans = 0
for i in range(L):
    ans += (ord(line[i]) - ord('a') + 1) * (r ** i)
ans %= M
print(ans)
