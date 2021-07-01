import sys
N = int(sys.stdin.readline())
total = list(map(int, sys.stdin.readline().split()))
total.sort()


def binary_search(array, target, start, end):
    if (end - start) <= 1:
        return end
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid)
    else:
        return binary_search(array, target, mid, end)

if N > 2:
    if min(total) >= 0:
        print(total[0], total[1])
    elif max(total) <= 0:
        print(total[-2], total[-1])
    else:
        index = binary_search(total, 0, 0, len(total) - 1)
        minus = total[:index]
        plus = total[index:]
        if len(plus) > 1 and len(minus) > 1:
            minimum = min(abs(sum(minus[-2:])), sum(plus[:2]))
            if minimum == abs(sum(minus[-2:])):
                ans = [minus[-2], minus[-1]]
            else:
                ans = [plus[0], plus[1]]
        elif len(plus) <= 1:
            minimum = abs(sum(minus[-2:]))
            ans = [minus[-2], minus[-1]]
        else:
            minimum = sum(plus[:2])
            ans = [plus[0], plus[1]]


        for i in minus:
            if plus[0] >= abs(i):
                idx = 0
                if i + plus[0] < minimum:
                    minimum = i + plus[0]
                    ans[0], ans[1] = i, plus[idx]
                    continue
                else:
                    continue
            elif plus[-1] <= abs(i):
                idx = len(plus) - 1
            else:
                idx = binary_search(plus, abs(i), 0, len(plus) - 1)


            if abs(i) == plus[idx]:
                print(i, plus[idx])
                sys.exit()
            elif idx == len(plus) - 1:
                if abs(i + plus[idx]) < minimum:
                    minimum = abs(i + plus[idx])
                    ans[0], ans[1] = i, plus[idx]
            else:
                check = min(abs(i) - plus[idx], plus[idx - 1] - abs(i))
                if check < minimum:
                    num = min([plus[idx], plus[idx - 1]], key = lambda x: abs(x-abs(i)))
                    minimum = check
                    ans[0], ans[1] = i, num
                else:
                    pass
            
        print(ans[0], ans[1])

else:
    print(total[0], total[1])

