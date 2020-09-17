# import sys
# sys.setrecursionlimit(10000)


def new_array(N):
    return [[False for i in range(10)] for _ in range(N)]


N, K = map(int, input().split())
M = [list(input()) for _ in range(N)]


ck = new_array(N)
ck2 = new_array(N)

dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]


def dfs(x, y):
    ck[x][y] = True
    ret = 1
    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]
        if xx < 0 or xx >= N or yy < 0 or yy >= 10:
            continue
        if M[xx][yy] != M[x][y] or ck[xx][yy]:
            continue
        ret += dfs(xx, yy)
    return ret


def dfs2(x, y, val):
    ck2[x][y] = True
    M[x][y] = '0'
    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]
        if xx < 0 or xx >= N or yy < 0 or yy >= 10:
            continue
        if M[xx][yy] != val or ck2[xx][yy]:
            continue
        dfs2(xx, yy, val)


def down():
    for i in range(10):
        tmp = []
        for j in range(N):
            if M[j][i] != '0':
                tmp.append(M[j][i])
        for j in range(N - len(tmp)):
            M[j][i] = '0'
        for j in range(N - len(tmp), N):
            M[j][i] = tmp[j-(N-len(tmp))]


while True:
    exist = False
    ck = new_array(N)
    ck2 = new_array(N)
    for i in range(N):
        for j in range(10):
            if M[i][j] == '0' or ck[i][j]:
                continue
            res = dfs(i, j)
            if res >= K:
                dfs2(i, j, M[i][j])
                exist = True
    if not exist:
        break
    down()


for i in M:
    print(''.join(i))
