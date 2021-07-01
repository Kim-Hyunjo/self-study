import sys

sys.stdin = open("input.txt", "r")

T = int(sys.stdin.readline().strip())

for _ in range(T):
    p = sys.stdin.readline().strip()
    n = int(sys.stdin.readline().strip())
    nums = sys.stdin.readline().strip()[1:-1].split(',')
    
    ro = 0
    first = 0
    last = 0
    
    for f in p:
        if f == 'R':
            ro += 1
        elif f == 'D':
            # 짝수번 뒤집었으면 앞에서, 아니라면 뒤에서 한개 뺄 것
            if ro % 2 == 0:
                first += 1
            else:
                last += 1

    if first + last <= n:
        nums = nums[first:n-last]
        
        if ro % 2 == 0:      
            print('['+','.join(nums)+']')
        else:
            print('['+','.join(nums[::-1])+']')
    else:
        print('error')


