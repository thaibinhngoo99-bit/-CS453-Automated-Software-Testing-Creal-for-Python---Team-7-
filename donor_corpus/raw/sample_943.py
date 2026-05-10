# BOJ 14501
import sys

si = sys.stdin.readline


t = [0] * 17
dp = [0] * 17

n = int(si())
for i in range(1, n + 1):
    m, o = map(int, si().split())
    t[i] = m
    dp[i] = o


def solve(n):
    ans = 0
    for i in range(n, 0, -1):
        if i + t[i] > n + 1:
            dp[i] = dp[i + 1]
        else:
            dp[i] = max(dp[i + 1], dp[i] + dp[i + t[i]])
            ans = max(ans, dp[i])
    return ans


print(solve(n))