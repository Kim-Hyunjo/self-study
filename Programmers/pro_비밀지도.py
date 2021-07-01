def solution(n, arr1, arr2):
    
    def setLen(num):
        if len(num) < n:
            num = '0'*(n-len(num)) + num
        return num
    
    answer = ["" for _ in range(n)]
    for i in range(n):
        bin1 = setLen(bin(arr1[i])[2:])
        bin2 = setLen(bin(arr2[i])[2:])
        for j in range(n):
            if bin1[j] == '0' and bin2[j] == '0':
                answer[i] += ' '
            else:
                answer[i] += '#'
                
    return answer