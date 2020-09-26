def solution(m, n, puddles):
    dp = [[0 for i in range(m+1)] for j in range(n+1)]
    for x, y in puddles:
        dp[y][x] = 'pad'
    dp[1][1] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue
            if dp[i][j] == 'pad':
                dp[i][j] = 0
                continue
            tmp = dp[i-1][j] + dp[i][j-1]
            dp[i][j] = tmp
    end = dp[-1][-1]
    return end % 1000000007
