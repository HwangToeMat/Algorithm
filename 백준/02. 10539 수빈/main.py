N, lst = int(input()), list(map(int, input().split()))

ans = []
ans.append(lst[0])

for _ in range(1, N):
    ans.append(((_+1) * lst[_]) - ((_) * lst[_-1]))

for i in ans:
    print(i, end=' ')
