from sys import stdin
import math

n, m = map(int, stdin.readline().split())

result = 100000
p = [0 for i in range(m)]
o = [0 for i in range(m)]

for i in range(m):
    p[i], o[i] = map(int,stdin.readline().split())

for i in p:
    t1 = i * math.ceil(n/6)
    t2 = i * (n // 6)
    for j in o:
        result = min(result, t1, j * n, t2 + (j * (n % 6)))

print(result)