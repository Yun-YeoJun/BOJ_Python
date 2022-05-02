from sys import stdin
import math

n = int(stdin.readline())
r1, r2 = 0,0

t = list(map(int,stdin.readline().split()))

for i in t:
    r1 += (i // 30 + 1) * 10
    r2 += (i // 60 + 1) * 15

if r1 < r2:
    print('Y',r1)
elif r1 == r2:
    print('Y','M',r1)
else:
    print('M',r2)