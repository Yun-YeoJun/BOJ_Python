from sys import stdin
from collections import deque

n, m, v = map(int, stdin.readline().split())

tree = {}

for i in range(1, n+1):
    tree[i] = []

for i in range(m):
    t1, t2 = map(int, stdin.readline().split())
    tree[t1].append(t2)
    tree[t2].append(t1)



resultBFS = []

def bfs(v):
    for i in range(1,n+1):
        tree[i] = sorted(tree[i])
    visited = [0 for i in range(n + 1)]
    queue = deque()
    visited[v] = 1
    resultBFS.append(v)
    queue.append(tree[v])
    while queue:
        l = queue.popleft()
        for i in l:
            if visited[i] == 1:
                continue
            resultBFS.append(i)
            visited[i] = 1
            queue.append(tree[i])


resultDFS = []
def dfs(v):
    for i in range(1,n+1):
        tree[i] = sorted(tree[i], reverse=True)
    stack = deque()
    visited = [0 for i in range(n + 1)]
    visited[v] = 1
    resultDFS.append(v)
    for i in tree[v]:
        stack.append(i)
    while stack:
        p = stack.pop()
        if visited[p] == 1:
            continue
        visited[p] = 1
        resultDFS.append(p)
        for i in tree[p]:
            stack.append(i)

dfs(v)
bfs(v)

for i in resultDFS:
    print(i, end=' ')
print()
for i in resultBFS:
    print(i, end=' ')
print()
