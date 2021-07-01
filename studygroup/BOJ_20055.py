from sys import stdin

N,K = map(int,stdin.readline().split())
durability = list(map(int,stdin.readline().split()))
robot=[False for _ in range(N)]  ##insert는 O(N) deque appendleft는 O(1)
step=0

while(durability.count(0) < K):  # durability 0인것 K개미만
    step += 1
    
    # 1단계
    a = durability.pop() 
    durability.insert(0,a)
    robot.pop()
    robot.insert(0,False)
    robot[N - 1] = False  # 내리는 칸 로봇 내림

    #2단계
    for i in range(N-2,0,-1):  # 뒤쪽부터 로봇 한 칸씩 이동
        # 현재 칸 기준 로봇이 있고, 다음 칸은 로봇없고, 내구도 0아닐때
        if robot[i] and not robot[i+1] and durability[i+1] != 0: 
            robot[i] = False
            robot[i+1] = True
            durability[i+1] -= 1
            if durability[i+1] < 0:
                durability[i+1] = 0
    robot[N - 1] = False
   
    # 3단계
    if durability[0] != 0 and not robot[0]:
        robot[0] = True
        durability[0] -= 1
        if durability[0] < 0:
            durability[0] = 0

print(step)
