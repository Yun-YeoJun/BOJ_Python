from sys import stdin

k, n, m = map(int, stdin.readline().split())

r = m - (k * n)

if r < 0:
    print(-r)
else:
    print(0)