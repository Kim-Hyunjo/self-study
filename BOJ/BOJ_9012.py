#9012 괄호

T = int(input())
for i in range(T):
    ps = input()
    sum = 0
    check = True
    for j in range(len(ps)):
        if ps[j] == '(':
            sum += 1
        elif ps[j] == ')':
            if sum <= 0:
                check = False
                break
            else:
                sum -= 1
    if sum == 0:
        if check == True:
            print('YES')
        if check == False:
            print('NO')
    else:
        print('NO')
