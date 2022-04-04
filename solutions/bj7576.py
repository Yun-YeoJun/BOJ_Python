from sys import stdin 
from collections import deque

m, n = map(int, stdin.readline().split()) # m : 가로, n : 세로

l = [[] for _ in range(n)]

cur_of_1 = []

for i in range(n):
    temp = list(map(int, stdin.readline().rstrip().split()))
    for j in temp:
        if j == 1:
            cur_of_1.append([i, len(l[i])])
        l[i].append(j)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()
for i in range(n):
    for j in range(m):
        if l[i][j] == 1:
            queue.append((i, j))
while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if l[nx][ny] == -1:
            continue
        if l[nx][ny] == 0 or l[nx][ny] > l[x][y] + 1:
            l[nx][ny] = l[x][y] + 1
            queue.append((nx,ny))

tf = True

for row in l:
    if 0 in row:
        print(-1)
        tf = False
        break

result = max(map(max, l))


if tf == True:
    result -= 1
    print(result)