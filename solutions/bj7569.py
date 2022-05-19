from sys import stdin
from collections import deque

m,n,h = map(int,stdin.readline().split())

tomato = [[[] for j in range(n)] for i in range(h)]
queue = deque()


for i in range(h):
    for j in range(n):
        tomato[i][j] = list(map(int,stdin.readline().split()))
        for k in range(len(tomato[i][j])):
            if tomato[i][j][k] == 1:
                queue.append((i,j,k,0))

visited = [[[0 for i in range(m)] for j in range(n)] for k in range(h)]
result = 0

dz = [0,0,-1,1,0,0]
dy = [0,0,0,0,-1,1]
dx = [-1,1,0,0,0,0]

def bfs(x,y,z,day):
    global result
    global queue
    visited[x][y][z] = 1
    while queue:
        x,y,z,day = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if nx < 0 or ny < 0 or nz < 0 or nx >= h or ny >= n or nz >= m:
                continue
            if tomato[nx][ny][nz] != 0:
                continue
            if visited[nx][ny][nz] == 1:
                continue
            visited[nx][ny][nz] = 1
            tomato[nx][ny][nz] = 1
            result = max(result, day + 1)
            queue.append((nx,ny,nz,day + 1))

if len(queue) != 0:
    x,y,z,day = queue[0]
    bfs(x,y,z,day)

for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 0:
                result = -1
                break
        if result == -1:
            break
    if result == -1:
        break

print(result)