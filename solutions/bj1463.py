from sys import stdin

n = int(stdin.readline())

l = [10**6 for _ in range(n + 1)]

l[1] = 0

cur = 1

while cur < n:
    if cur * 3 <= n and l[cur * 3] > l[cur] + 1:
        l[cur * 3] = l[cur] + 1
    if cur * 2 <= n and l[cur * 2] > l[cur] + 1:
        l[cur * 2] = l[cur] + 1
    if cur + 1 <= n and l[cur + 1] > l[cur] + 1:
        l[cur + 1] = l[cur] + 1
    cur += 1

print(l[n])