N = int(input())


def sol(N):
    ans = [0] * 100000
    ans[1] = 1
    ans[2] = 2
    for _ in range(3, N+1):
        ans[_] = ans[_-1] + ans[_-2]
    return ans[N] % 15746


A = sol(N)
print(A)
