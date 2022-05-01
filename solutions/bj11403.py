from sys import stdin
from collections import deque

n = int(stdin.readline())

l = {}

for i in range(n):
    l[i] = []

for i in range(n):
    temp = list(map(int,stdin.readline().split()))
    for j in range(n):
        if temp[j] == 1:
            l[i].append(j)

def bfs(x, target):
    result = 0
    queue = deque()
    visited = [0 for a in range(n)]
    queue.append(x)
    while queue:
        x = queue.popleft()
        t = l[x]
        for k in t:
            if visited[k] == 1:
                continue
            if target == k:
                result = 1
                break
            visited[k] = 1
            queue.append(k)
    return result

for i in range(n):
    for j in range(n):
        print(bfs(i,j), end=' ')
    print()