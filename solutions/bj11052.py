import sys
input = sys.stdin.readline

n = int(input())
p = list(map(int,input().split()))

l = {}

l[0] = 0
l[1] = p[0]

def dp(k):
    if k in l:
        return l[k]
    M = p[k-1]
    if k == 0:
        return 0
    elif k == 1:
        return l[1]
    else:
        for i in range(1,k):
            temp = dp(i) * (k // i) + dp(k % i)
            if M < temp:
                M = temp
        l[k] = M
        return M

print(dp(n))