import sys
import heapq

def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1

        if left > right:
            array[pivot], array[right] = array[right], array[pivot]
        else:
            array[left], array[right] = array[right], array[left]
        
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


def binary_search(array, target, start, end):
    if start > end:
        return None
    if end - start <= 1:
        return end

    mid = (start + end) // 2
    if array[mid] == target:
        return array[mid]
    elif array[mid] > target:
        return binary_search(array, target, start, mid)
    elif array[mid] < target:
        return binary_search(array, target, mid, end)


input = sys.stdin.readline
N, K = map(int, input().split())
gems, bags = [], []
for _ in range(N):
    a, b = map(int, input().split())
    heapq.heappush(gems, [-b, a])
for _ in range(K):
    bags.append(int(input()))


quick_sort(bags, 0, len(bags) - 1)
ans = 0
for _ in range(N):
    price, weight = heapq.heappop(gems)
    real_price = -price
    if len(bags) > 0:
        if weight <= bags[-1]:
            idx = binary_search(bags, weight, 0, len(bags) - 1)
            del bags[idx]
            ans += real_price
    else:
        break

print(ans)
