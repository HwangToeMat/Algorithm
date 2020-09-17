N = int(input())
T = [list(map(int, input().split())) for _ in range(N)]

A = [[0 for _ in range(N+1)] for i in range(N+1)]
DP = [[0 for _ in range(N+1)] for i in range(N+1)]

for i in range(1, N + 1):
    cnt = 0
    for _ in T[i - 1]:
        cnt += 1
        A[i][cnt] = _

for i in range(1, N+1):
    for j in range(1, N+1):
        DP[i][j] = max(DP[i-1][j], DP[i-1][j-1]) + A[i][j]

print(max(DP[-1]))
