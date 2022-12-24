import sys
input = sys.stdin.readline
from collections import deque

n = int(input())

tree = {}

for i in range(1, n + 1):
    tree.update({i:[]})

for i in range(n-1):
    a,b=map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

queue = deque()

result = [-1 for i in range(n + 1)]

for i in tree[1]:
    queue.append(i)
    result[i] = 1

while queue:
    m = queue.popleft()

    for i in tree[m]:
        if result[i] != -1:
            continue
        queue.append(i)
        result[i] = m

for i in result[2:]:
    print(i)
