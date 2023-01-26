import sys
input = sys.stdin.readline

n = int(input())

a = list(map(int,input().split()))

dp = [[1 for i in range(2)] for i in range(n)]

for i in range(n):
    for j in range(i):
        if a[i] >a[j]:
            dp[i][0] = max(dp[i][0],dp[j][0]+1)

for i in reversed(range(n)):
    for j in reversed(range(i+1,n)):
        if a[i] > a[j]:
            dp[i][1] = max(dp[i][1],dp[j][1]+1)


result = 0

for i in range(n):
    result = max(result,dp[i][0]+dp[i][1])

print(result-1)