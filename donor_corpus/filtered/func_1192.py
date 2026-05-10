def solve(n):
    ans = 0
    for i in range(n, 0, -1):
        if i + t[i] > n + 1:
            dp[i] = dp[i + 1]
        else:
            dp[i] = max(dp[i + 1], dp[i] + dp[i + t[i]])
            ans = max(ans, dp[i])
    return ans