from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())

graph = {}

for i in range(n):
    graph[i + 1] = []

for i in range(m):
    t1, t2 = map(int, stdin.readline().split())
    graph[t1].append(t2)
    graph[t2].append(t1)

visited = [0] * (n + 1)
queue = deque()
result = 0
keysOfGraph = list(graph.keys())

for i in keysOfGraph:
    if visited[i] == 0:
        queue.append(graph[i])
        visited[i] = 1

        while queue:
            temp = queue.popleft()
            for k in temp:
                if visited[k] == 0:
                    visited[k] = 1
                    queue.append(graph[k])
        result += 1

print(result)