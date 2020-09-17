from copy import deepcopy
N = int(input())
A = list(map(int, input().split()))

dp = deepcopy(A)

for i in range(1, N):
    for _ in range(i):
        if A[i] > A[_]:
            dp[i] = max(A[i] + dp[_], dp[i])

print(max(dp))
