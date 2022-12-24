import sys
input = sys.stdin.readline

n, k = map(int,input().split())

w = [0 for i in range(n)]
v = [0 for i in range(n)]

for i in range(n):
    w[i],v[i] = map(int,input().split())

w = [0] + w
v = [0] + v

dp = [[0 for i in range(k + 1)] for j in range(n + 1)]

for i in range(1,n+1):
    for j in range(1,k+1):
        if w[i] <= j:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-w[i]]+v[i])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[n][k])