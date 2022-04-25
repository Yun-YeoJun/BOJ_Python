from sys import stdin

n, m = map(int, stdin.readline().split())

site = {}

for i in range(n):
    t1, t2 = stdin.readline().split()
    site[t1] = t2

for i in range(m):
    print(site[stdin.readline().rstrip()])