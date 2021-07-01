
# 1. 문제, 입력, 출력읽고 로컬에 코드작성
# 2. 예제 입력 복사해서 터미널에서 확인 / 

import sys

sys.stdin = open("input.txt", "r")

A,B = map(int,sys.stdin.readline().split())
print(A+B)