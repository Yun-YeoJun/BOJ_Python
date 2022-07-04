import sys
from collections import deque
input = sys.stdin.readline

n,m=map(int,input().split())
l = [0 for i in range(n)]

for i in range(n):
    l[i] = list(map(int,list(input().rstrip())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]


if n == m == 1:
    result = 1
else:
    queue = deque()
    queue.append((0,0,1,0))
    visited = [[0 for i in range(m)] for j in range(n)]
    visited[0][0] = 1
    result = -1
    while queue:
        x,y,leng,wall = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            nwall = wall
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if visited[nx][ny] != 0:
                if visited[nx][ny] == 2:
                    continue
                if visited[nx][ny] == 1 and nwall == 1:
                    continue
            if l[nx][ny] == 1:
                if wall == 1:
                    continue
                else:
                    nwall = 1
            else:
                if nwall == 1:
                    visited[nx][ny] = 1
                else:
                    visited[nx][ny] = 2
            if result == -1:
                if nx == n - 1 and ny == m - 1:
                    result = leng + 1
            else:
                if nx == n - 1 and ny == m - 1:
                    if result > leng + 1:
                        result = leng + 1
            queue.append((nx,ny,leng+1,nwall))


print(result)