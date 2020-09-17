c = [0 for _ in range(3)]
m = [0 for _ in range(3)]
for _ in range(3):
    c[_], m[_] = map(int, input().split())

for _ in range(100):
    cnt = _ % 3
    if cnt + 1 == 3:
        next_cnt = 0
    else:
        next_cnt = cnt+1
    tmp = m[cnt] + m[next_cnt]
    m[next_cnt] = min(tmp, c[next_cnt])
    m[cnt] = max(tmp - c[next_cnt], 0)

for _ in m:
    print(_)
