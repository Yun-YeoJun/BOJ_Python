from sys import stdin
from collections import deque

t = int(stdin.readline())

for testcase in range(t):
    m, n, k = map(int, stdin.readline().split())
    l = [[0 for i in range(m)] for j in range(n)]

    for i in range(k):
        x, y = map(int, stdin.readline().split())

        l[y][x] = 1
    
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    cnt = 0

    for i in range(n):
        for j in range(m):
            if l[i][j] == 1:
                queue = deque()
                queue.append((i,j))
                cnt += 1

                while queue:
                    x, y = queue.popleft()

                    l[x][y] = 0

                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if nx < 0 or ny < 0 or nx >= n or ny >= m:
                            continue
                        if l[nx][ny] == 0:
                            continue
                        l[nx][ny] = 0
                        queue.append((nx, ny))

    print(cnt)