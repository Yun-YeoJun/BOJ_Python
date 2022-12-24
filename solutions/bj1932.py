import sys
input = sys.stdin.readline

n = int(input())

l = [[] for i in range(n)]

for i in range(n):
    l[i] = list(map(int,input().split()))

dp = [[-1 for i in range(n)] for j in range(n)]

def calc_max(step,idx):
    if step == n - 1:
        return l[step][idx]
    if dp[step][idx] == -1:
        dp[step][idx] = l[step][idx] + max(calc_max(step + 1, idx),calc_max(step+1,idx+1))
        return dp[step][idx]
    else:
        return dp[step][idx]

print(calc_max(0,0))