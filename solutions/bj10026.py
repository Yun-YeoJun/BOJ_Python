from sys import stdin
from collections import deque

n = int(stdin.readline())
l = []

for i in range(n):
    l.append(list(stdin.readline().rstrip()))

visited = [[0 for i in range(n)] for j in range(n)]

def bfs(x, y, color):
    #visited = [[0 for i in range(n)] for j in range(n)]
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if visited[nx][ny] == 1:
                continue
            if l[nx][ny] == color:
                visited[nx][ny] = 1
                queue.append((nx,ny))

def oddBfs(x, y, color):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    if color == 'B':
        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                if visited[nx][ny] == 1:
                    continue
                if l[nx][ny] == color:
                    visited[nx][ny] = 1
                    queue.append((nx,ny))
    else:
        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                if visited[nx][ny] == 1:
                    continue
                if l[nx][ny] == 'R' or l[nx][ny] == 'G':
                    visited[nx][ny] = 1
                    queue.append((nx,ny))

result1 = 0


for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j, l[i][j])
            result1 += 1

visited = [[0 for i in range(n)] for j in range(n)]
result2 = 0

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            oddBfs(i, j, l[i][j])
            result2 += 1

print(result1, result2)