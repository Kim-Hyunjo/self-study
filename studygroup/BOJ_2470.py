import sys

n = int(sys.stdin.readline())
sol = sorted(list(map(int,sys.stdin.readline().split())))

start, end = 0, n-1
lowest = sys.maxsize
liq1, liq2 = 0, 0

while start < end:
    if abs(sol[start] + sol[end]) < lowest:
        lowest = abs(sol[start] + sol[end])
        liq1, liq2 = sol[start], sol[end]
    else:
        if abs(sol[start]) < abs(sol[end]):
            end -= 1
        else:
            start += 1

print(liq1, liq2)