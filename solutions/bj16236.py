from sys import stdin
from collections import deque

n = int(stdin.readline())
result = 0
sharkX = -1
sharkY = -1
sharkSize = 2
eatCnt = 0
visited = [[0 for i in range(n)] for j in range(n)]
l = []

for i in range(n):
    l.append(list(map(int,stdin.readline().split())))
    for j in range(n):
        if l[i][j] == 9:
            sharkX = i
            sharkY = j

# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    minCnt, minX, minY = -1, -1, -1
    global sharkX
    global sharkY
    global result
    global eatCnt
    global sharkSize
    queue = deque()
    visited[x][y] = 1
    queue.append((x,y,1))
    while queue:
        x,y,cnt = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if visited[nx][ny] == 1:
                continue
            if 0 < l[nx][ny] < sharkSize:
                if minCnt == -1:
                    minCnt = cnt
                    minX = nx
                    minY = ny
                    eatCnt += 1
                else:
                    if minCnt >= cnt:
                        if minCnt > cnt:
                            minCnt = cnt
                            minX = nx
                            minY = ny
                        else:
                            if minX > nx:
                                minCnt = cnt
                                minX = nx
                                minY = ny
                            elif minX == nx:
                                if minY > ny:
                                    minCnt = cnt
                                    minX = nx
                                    minY = ny
            elif l[nx][ny] == 0 or l[nx][ny] == sharkSize:
                visited[nx][ny] = 1
                queue.append((nx,ny,cnt + 1))
            else:
                continue

    if eatCnt == sharkSize:
        sharkSize += 1
        eatCnt = 0
    if minCnt != -1:
        result += minCnt
        l[sharkX][sharkY] = 0
        l[minX][minY] = 9
        sharkX = minX
        sharkY = minY
        return 0
    else:
        return 1


tf = 0

while tf == 0:
    tf = bfs(sharkX,sharkY)
    visited = [[0 for i in range(n)] for j in range(n)]

print(result)