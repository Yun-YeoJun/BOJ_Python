import sys
input = sys.stdin.readline
MOD = 1000000007

n = int(input())

def matrixMult(a,b):
    l = [[0,0],[0,0]]
    l[0][0] = a[0][0] * b[0][0] % MOD + a[0][1] * b[1][0] % MOD
    l[1][0] = a[1][0] * b[0][0] % MOD + a[1][1] * b[1][0] % MOD
    l[0][1] = a[0][0] * b[0][1] % MOD + a[0][1] * b[1][1] % MOD
    l[1][1] = a[1][0] * b[0][1] % MOD + a[1][1] * b[1][1] % MOD
    return l

def fib(n):
    if n == 1:
        return [[1,1],[1,0]]
    temp = fib(n // 2)
    if n % 2 == 1:
        return matrixMult(matrixMult(temp,temp),fib(1))
    else:
        return matrixMult(temp,temp)

    

print(fib(n)[1][0] % MOD)