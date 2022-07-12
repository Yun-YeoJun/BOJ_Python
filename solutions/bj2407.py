import sys
import itertools
input = sys.stdin.readline

n,m = map(int,input().split())


fac = {0:1,1:1}

def factorial(k):
    if k in fac:
        return fac[k]
    else:
        fac[k] = factorial(k - 1) * k
        return fac[k]

nFac = factorial(n)
mFac = factorial(m)
nMmFac = factorial(n-m)

print(nFac // (mFac * nMmFac))