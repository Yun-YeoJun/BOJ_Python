import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())

graph = [[] for i in range(n)]

for i in range(n):
    graph[i] = list(map(int,input().split()))

time = 0

def bfs():
    global n
    global m
    global time

    visited = [[0 for i in range(m)] for j in range(n)]

    count = {}

    queue = deque()

    queue.append((0,0))

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if visited[nx][ny] == 1:
                continue

            if graph[nx][ny] == 1:
                if (nx,ny) in count:
                    count[(nx,ny)] += 1
                else:
                    count[(nx,ny)] = 1

            else:
                queue.append((nx,ny))
                visited[nx][ny] = 1



    for i in count:
        if count[i] >= 2:
            x,y = i
            graph[x][y] = 0

    if len(count) != 0:
        time += 1
        return True
    else:
        return False

tf = bfs()
while tf:
    tf = bfs()


print(time)