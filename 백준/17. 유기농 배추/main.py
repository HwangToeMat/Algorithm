import sys
sys.setrecursionlimit(10000)

T = int(input())

dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]

B = []
ck = []


def dfs(x, y):
    global B, ck
    if ck[y][x] == 1:
        return
    ck[y][x] = 1
    for _ in range(4):
        if B[y + dy[_] + 1][x + dx[_] + 1] == 0:
            continue
        elif ck[y + dy[_]][x + dx[_]] == 1:
            continue
        elif B[y + dy[_] + 1][x + dx[_] + 1] == 1:
            dfs(x + dx[_], y + dy[_])


def process():
    global B, ck
    M, N, K = map(int, input().split())
    B = [[0 for i in range(M+2)] for j in range(N+2)]
    ck = [[0 for i in range(M)] for j in range(N)]
    ans = 0
    for _ in range(K):
        x, y = map(int, input().split())
        B[y+1][x+1] = 1
    for i in range(M):
        for j in range(N):
            if ck[j][i] == 1 or B[j+1][i+1] == 0:
                continue
            else:
                dfs(i, j)
                ans += 1
    return ans


for _ in range(T):
    print(process())
