import collections

people = collections.deque()
N, K = map(int, input().split())
ans = "<"
for i in range(N):
    people.append(i+1)
for i in range(N):
    people.rotate(-K+1)
    new_ans = [ans]
    new_ans.append(str(people.popleft()))
    ans = ''.join(new_ans)
    if i != N-1:
        new_ans.append(', ')
        ans = ''.join(new_ans)
    else:
        new_ans.append('>')
        ans = ''.join(new_ans)
print(ans)