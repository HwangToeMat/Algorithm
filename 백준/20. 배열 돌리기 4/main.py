from copy import deepcopy
N, M, K = map(int, input().split())
ret = 10000
A = [list([0 for m in range(M+2)])] + [[0] + list(map(int, input().split())) + [0]
                                       for _ in range(N)] + [list([0 for m in range(M+2)])]

ans = 1000000
Rotate = [list(map(int, input().split())) for _ in range(K)]


def new_arr():
    return [[0 for m in range(M+2)] for n in range(N+2)]


def min_arr(A):
    return min(map(sum, A[1:-1]))


def rot_arr(Arr, R, C, S):
    A = deepcopy(Arr)
    ck = new_arr()
    ck[R][C] = A[R][C]
    for s in range(1, S+1):
        ck[R - s][C - s + 1: C + s + 1] = A[R - s][C - s: C + s]
        for tmp in range(2 * s):
            ck[R - s + 1 + tmp][C + s] = A[R - s + tmp][C + s]
        ck[R + s][C - s: C + s] = A[R + s][C - s + 1: C + s + 1]
        for tmp in range(2 * s):
            ck[R - s + tmp][C - s] = A[R - s + 1 + tmp][C - s]
    for i in range(M+2):
        for j in range(N+2):
            if ck[j][i] == 0:
                continue
            else:
                A[j][i] = ck[j][i]
    return A


def dfs(Arr, cnt):
    global ans
    if sum(cnt) == K:
        ans = min(ans, min_arr(Arr))
        return
    for _ in range(K):
        if cnt[_]:
            continue
        r, c, s = Rotate[_]
        new = rot_arr(Arr, r, c, s)
        cnt[_] = 1
        dfs(new, cnt)
        cnt[_] = 0


dfs(A, [0 for _ in range(K)])
print(ans)
