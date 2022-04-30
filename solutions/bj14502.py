from sys import stdin
from collections import deque
import copy

n, m = map(int, stdin.readline().split())

l = []

for i in range(n):
    l.append(list(map(int,stdin.readline().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs1(x,y):
    queue = deque()
    visited = [[0 for i in range(m)] for j in range(n)]
    visited[x][y] = 1
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if visited[nx][ny] == 1:
                continue
            if tl[nx][ny] == 1 or tl[nx][ny] == 2:
                continue
            tl[nx][ny] = 2
            visited[nx][ny] = 1
            queue.append((nx,ny))

def bfs2(x,y):
    queue = deque()
    visited = [[0 for i in range(m)] for j in range(n)]
    visited[x][y] = 1
    queue.append((x,y))
    tl[x][y] = 1
    cnt = 1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if visited[nx][ny] == 1:
                continue
            if tl[nx][ny] == 1:
                continue
            cnt += 1
            visited[nx][ny] = 1
            queue.append((nx,ny))
            tl[nx][ny] = 1
    return cnt

x1, x2, x3, y1, y2, y3 = -1,-1,-1,-1,-1,-1
result = 0

for i in range(n):
    for j in range(m):
        if l[i][j] == 0:
            x1 = i
            y1 = j
            for a in range(i, n):
                for b in range(m):
                    if a == i and b == j:
                        continue
                    if l[a][b] == 0:
                        x2 = a
                        y2 = b
                        for c in range(a,n):
                            for d in range(m):
                                if c == a and d == b:
                                    continue
                                if c == i and d == j:
                                    continue
                                if l[c][d] == 0:
                                    x3 = c
                                    y3 = d
                                    tempResult = 0
                                    tl = copy.deepcopy(l)
                                    tl[x1][y1] = 1
                                    tl[x2][y2] = 1
                                    tl[x3][y3] = 1
                                    for x in range(n):
                                        for y in range(m):
                                            if tl[x][y] == 2:
                                                bfs1(x,y)
                                    for x in range(n):
                                        for y in range(m):
                                            if tl[x][y] == 0:
                                                tempResult += bfs2(x,y)
                                    result = max(result, tempResult)

print(result)                                    