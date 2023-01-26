import sys
input = sys.stdin.readline

n, b = map(int,input().split())

matrix = [list(map(int,input().split())) for i in range(n)]

is_even = lambda x: x % 2 == 0

def cross_product(a,b):
    global n
    result = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += a[i][k] * b[k][j]
            result[i][j] %= 1000

    return result

def calc_pow(k):
    if k == 1:
        return matrix
    
    if is_even(k):
        temp = calc_pow(k // 2)
        return cross_product(temp,temp)

    else:
        temp = calc_pow(k - 1)
        return cross_product(temp,matrix)

result = calc_pow(b)

for i in result:
    for j in i:
        print(j % 1000,end=' ')
    print()
