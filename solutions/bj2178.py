from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split()) # n : 세로, m : 가로

l = [[] for _ in range(n)]

for i in range(n):
    temp = stdin.readline().rstrip()
    for j in list(temp):
        l[i].append(int(j))

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()

queue.append((0, 0))

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i] # 세로
        ny = y + dy[i] # 가로

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if l[nx][ny] == 0:
            continue
        if l[nx][ny] == 1:
            l[nx][ny] = l[x][y] + 1
            queue.append((nx, ny))

print(l[n-1][m-1])