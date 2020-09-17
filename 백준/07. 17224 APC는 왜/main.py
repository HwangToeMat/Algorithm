N, L, K = map(int, input().split())
count = 0
count_2 = 0

for _ in range(N):
    sub_1, sub_2 = map(int, input().split())
    if sub_1 <= L and sub_2 <= L:
        count += 1
        if count == K:
            break
    elif sub_1 <= L:
        count_2 += 1
    else:
        break

if K - count > 0:
    if K - count >= count_2:
        score = 140*count + 100*count_2
    else:
        score = 140*count + 100*(K - count)
else:
    score = 140*K


print(score)
