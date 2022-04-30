from sys import stdin 
from collections import deque

h, w = map(int, stdin.readline().split())

l = []

for i in range(h):
    l.append(list(stdin.readline().rstrip()))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    visited = [[0 for i in range(w)] for j in range(h)]
    visited[x][y] = 1
    max = 0
    queue.append((x,y,0))
    while queue:
        x,y,t = queue.popleft()
        if max < t:
            max = t
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if visited[nx][ny] == 1:
                continue
            if l[nx][ny] == 'W':
                continue
            visited[nx][ny] = 1
            queue.append((nx,ny,t + 1))
    return max

result = 0

for i in range(h):
    for j in range(w):
        if l[i][j] == 'L':
            result = max(result, bfs(i,j))

print(result)