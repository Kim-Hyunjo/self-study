from sys import stdin

N = int(stdin.readline())
towerList = list(map(int, stdin.readline().rstrip().split()))
resultList = [0 for _ in range(N)]
stack = []

for i in range(len(towerList)-1, -1, -1):
    # stack이 비어있다면 [탑 번호, 탑 높이] 를 넣음
    if len(stack) == 0:
        stack.append([i, towerList[i]])
    # stack이 비어있지 않다면, 현재 높이가 stack에 있는 높이보다 높을 동안
    # pop해줌
    else:
        while towerList[i] > stack[len(stack)-1][1]:
            tower = stack.pop()
            resultList[tower[0]] = i+1
            if len(stack) == 0:
                break
        
        stack.append([i,towerList[i]])

for num in resultList:
    print(num,end=" ")