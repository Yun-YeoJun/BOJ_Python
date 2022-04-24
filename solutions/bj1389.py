from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split()) # n : 유저의 수, m : 친구 관계의 수

graph = {}

for i in range(1, n + 1):
    graph[i] = []

for i in range(m):
    a, b = map(int, stdin.readline().split())
    al = graph.get(a)
    bl = graph.get(b)

    al.append(b)
    bl.append(a)

    graph[a] = al
    graph[b] = bl

result = [-1] * n

for i in range(1, n + 1):
    tempResult = [-1] * n
    tempResult[i - 1] = 0
    queue = deque()
    queue.append((graph[i], 0))
    while queue:
        friends, length = queue.popleft()
        for j in friends:
            if tempResult[j - 1] == -1:
                tempResult[j - 1] = length + 1
                queue.append((graph[j],length + 1))
    result[i - 1] = sum(tempResult)

tmp = min(result)
idx = result.index(tmp)

print(idx + 1)