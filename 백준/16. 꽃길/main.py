N = int(input())

G = [list(map(int, input().split())) for _ in range(N)]

dx, dy = [0, 0, -1, 0, 1], [0, 1, 0, -1, 0]
ans = 9999999


def chk(lst):
    ret = 0
    tmp = []
    for _ in lst:
        x = _ % N
        y = _ // N
        if x <= 0 or x >= N-1 or y <= 0 or y >= N-1:
            return 100000
        for d in range(5):
            ret += G[y + dy[d]][x + dx[d]]
            tmp.append((x + dx[d], y + dy[d]))
    if len(set(tmp)) != len(tmp):
        return 100000
    return ret


for i in range(N*N):
    for j in range(N*N):
        for k in range(N*N):
            ans = min(ans, chk([i, j, k]))

print(ans)
