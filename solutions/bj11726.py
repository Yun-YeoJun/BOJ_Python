from sys import stdin

n = int(stdin.readline())

cnt = 0
dp = [-1 for i in range(n)]
dp[0] = 1
dp[1] = 2

for i in range(2, n):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n - 1] % 10007)