from sys import stdin

dp = {1 : 1, 2 : 1, 3 : 1}

def sequence(x):
    if x in dp:
        return dp[x]
    else:
        dp[x] = sequence(x - 2) + sequence(x - 3)
        return dp[x] 
    

t = int(stdin.readline())

for i in range(t):
    n = int(stdin.readline())
    print(sequence(n))