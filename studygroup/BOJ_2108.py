import sys

N = int(sys.stdin.readline())
nums = []
# count[idx]: idx - 4000의 나타난 횟수
count = [0 for _ in range(8001)]  
for _ in range(N):
    num = int(sys.stdin.readline())
    nums.append(num)
    count[num+4000] += 1

nums.sort()
cnt_dict = {}
for idx, cnt in enumerate(count):
    if cnt != 0:
        cnt_dict[idx] = cnt

freq_idx = 0
# cnt에 대해 오름차순, idx에 대해 내림차순 정렬
cnt_items = sorted(cnt_dict.items(), key=lambda kv: (kv[1], -kv[0]))
if len(cnt_items) == 1:
    freq_idx = cnt_items[0][0]
elif cnt_items[-1][1] != cnt_items[-2][1]:
    freq_idx = cnt_items[-1][0]
else:
    freq_idx = cnt_items[-2][0]

print(int(round(sum(nums)/N, 0)))
print(nums[N // 2])
print(freq_idx-4000)
print(nums[-1] - nums[0])