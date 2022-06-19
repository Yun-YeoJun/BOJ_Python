import sys
from collections import deque
input = sys.stdin.readline

n,m=map(int,input().split())

graph = {}

for i in range(1,101):
    graph[i] = i

for i in range(n + m):
    x,y = map(int,input().split())
    graph[x] = y

def bfs(graph):
    queue = deque()
    queue.append((1,0))
    result = -1
    visited = [0 for i in range(101)]
    while queue:
        cur, cnt = queue.popleft()
        for i in range(1,7):
            if cur + i > 100:
                continue
            next = graph[cur + i]
            
            if next == 100:
                result = cnt + 1
                break
            if visited[next] == 1:
                continue
            queue.append((next,cnt + 1))
            visited[next] = 1
        if result != -1:
            break
    return result

print(bfs(graph))