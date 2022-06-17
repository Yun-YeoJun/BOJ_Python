import sys
input = sys.stdin.readline

n, m = map(int, input().split())

l = list(map(int,input().split()))

prefixSum = [0 for i in range(n)]
prefixSum[0] = l[0]

for i in range(1,n):
    prefixSum[i] = prefixSum[i - 1] + l[i]

for _ in range(m):
    i,j = map(int,input().split())
    if i == 1:
        print(prefixSum[j - 1])
    else:
        print(prefixSum[j - 1] - prefixSum[i - 2])