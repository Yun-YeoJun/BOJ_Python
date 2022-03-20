from sys import stdin 

def fib(n, l0, l1):
    if n == 0:
        l0[0] = 1
    elif n == 1:
        l1[1] = 1
    else:
        l1[n] = l1[n - 1] + l1[n - 2]
        l0[n] = l0[n - 1] + l0[n - 2]

t = int(stdin.readline())

for _ in range(t):
    n = int(stdin.readline())
    l0 = [0 for z in range(n + 1)]
    l1 = [0 for z in range(n + 1)]
    result0 = 0
    result1 = 0
    if n == 0:
        l0[0] = 1
        result0 = 1
    elif n == 1:
        l1[1] = 1
        result1 = 1
    else:
        for i in range(n + 1):
            fib(i, l0, l1)

        result0 = l0[n]
        result1 = l1[n]
    print("%d %d" %(result0, result1))