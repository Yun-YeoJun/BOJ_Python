from sys import stdin 
from collections import deque

n = int(stdin.readline()) # n * n 정사각형
l = []

for i in range(n):
    l.append(list(map(int, stdin.readline().rstrip())))

def bfs(x, y):
    queue = deque()

    queue.append((x,y))
    cnt = 1
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        x, y = queue.popleft()
        l[x][y] = 0
        #cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 지도 밖으로 나가는 지 체크
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if l[nx][ny] == 0:
                continue
            if l[nx][ny] == 1:
                queue.append((nx,ny))
                cnt += 1
                l[nx][ny] = 0
    return cnt

result = []

for i in range(n):
    for j in range(n):
        if l[i][j] == 1:
            result.append(bfs(i,j))

result = sorted(result)

print(len(result))
for r in result:
    print(r)