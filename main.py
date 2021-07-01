def main():
    x = input()
    cnt = 0
    for b in x:
        if b == "(":
            cnt += 1
        elif b == ")":
            cnt -= 1
    if cnt == 0:
        print("YES")
    else:
        print("NO")

if __name__=="__main__":
    main()