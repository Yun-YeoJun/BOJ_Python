from sys import stdin
from collections import deque

# n : numbers of computers, m : numbers of edges
n = int(stdin.readline())
m = int(stdin.readline())

tree = {}

for i in range(1, n + 1):
    tree[i] = []

for i in range(m):
    t1, t2 = map(int, stdin.readline().split())
    tree[t1].append(t2)
    tree[t2].append(t1)

visitied = [0] * n
queue = deque()

keysOfTree = list(tree.keys())
visitied[keysOfTree[0]-1] = 1
queue.append(tree[keysOfTree[0]])

while queue:
    temp = queue.popleft()
    for i in temp:
        if visitied[i - 1] == 0:
            visitied[i - 1] = 1
            queue.append(tree[i])

result = 0
for i in visitied:
    if i == 1:
        result += 1
result -= 1
print(result)