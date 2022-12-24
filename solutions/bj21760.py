import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n,m,k,d = map(int,input().split())
    p = m ** n
    q = m * (m - 1)
    b = 1
    a = b * k
    while p * b + q * a <= d:
        b+=1
        a=b*k
    if p * (b - 1) + q * (b - 1) * k == 0:
        print(-1)
    else:
        print(p * (b - 1) + q * (b - 1) * k)