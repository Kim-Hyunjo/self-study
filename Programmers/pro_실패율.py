def solution(N, stages):
    #실패율: (현 스테이지 실패자 수) / (전 스테이지 도전자 - 전 스테이지 실패자) 
    failures = [0 for _ in range(N)]
    for s in stages:
        if s != N+1:
            failures[s-1] += 1
    last = len(stages)
    fail_pers = {0:failures[0]/last}    
    for i in range(1,N):
        last -= failures[i-1]
        if last != 0:
            fail_pers[i] = failures[i] / last
        else:
            for j in range(i,N):
                fail_pers[j] = 0
            break
    items = fail_pers.items()
    sorted_pers = sorted(items, key=lambda item:(-item[1],item[0]))       
    answer = [s[0]+1 for s in sorted_pers]
    return answer