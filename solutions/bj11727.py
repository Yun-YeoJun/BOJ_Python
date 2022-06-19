import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
dp = [0 for i in range(n)]
dp[0] = 1
dp[1] = 3


for i in range(2,n):
    dp[i] = dp[i - 1] + dp[i - 2] * 2
print(dp[n-1] % 10007)