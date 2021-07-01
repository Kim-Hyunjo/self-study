from collections import deque
import sys
N= int(sys.stdin.readline())
tower_queue= deque(list(map(int, sys.stdin.readline().split())))

ans= ''

check= deque()
for i in range(len(tower_queue)):  # 500000
    v= tower_queue.popleft()
    if len(check) > 0:
        num= 0
        for s in check:
            num += 1
            if s > v:
                ans += str(len(check) - num + 1)
                check.appendleft(v)
                break
            else:
                if s == check[-1]:
                    ans += '0'
                    check.appendleft(v)
                    break
                else:
                    pass
            

    else:
        ans += '0'
        check.appendleft(v)

print(' '.join(ans))

        
# 9 5 7 4    
