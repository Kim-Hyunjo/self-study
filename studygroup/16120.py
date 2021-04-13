#16120 PPAP
import sys

line = sys.stdin.readline()
if line == "P" or line == "PPAP":
    print("PPAP")
else:
    stack = []
    ppap = ["P","P","A","P"]
    for c in line:
        stack.append(c)  # stack에 line의 문자를 앞에서부터 넣는다.
        if len(stack) >= 4 and stack[-4:] == ppap:  # stack의 끝에서 4번째 인덱스부터 끝까지가 "PPAP"라면
            for _ in range(3):
                stack.pop()  # "P"를 제외한 뒤의 세개의 문자("P","A","P")를 pop한다.
    result = ''.join(stack)
    if result == "PPAP" or result == "P":
        print("PPAP")
    else:
        print("NP")