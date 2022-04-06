from sys import stdin
from collections import deque
#import numpy as np
from itertools import combinations

n, m = map(int, stdin.readline().split()) # n: 세로, m: 가로

l = []

for i in range(n):
    t = stdin.readline().rstrip()
    l.append(list(map(int,t.split())))

def bfs(x, y):
    visited = [[0 for a in range(m)] for b in range(n)]
    queue = deque()

    queue.append((x,y))
    
    #상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if temp[nx][ny] == 0:
                if visited[nx][ny] == 0:
                    temp[nx][ny] = 2
                    queue.append((nx,ny))
                    visited[nx][ny] = 1

#flatL = np.array(l).flatten().tolist()
l0 = []
for i in range(n):
    for j in range(m):
        if l[i][j] == 0:
            l0.append((i,j))

permutation_0 = list(combinations())
print(permutation_0)
l2 = []
for i in range(n):
    for j in range(m):
        if l[i][j] == 2:
            l2.append((i,j))

result = 0
for i in range(n * m):
    xi = i // m
    yi = i % m
    if l[xi][yi] == 0:
        for j in range(i + 1, n * m):
            xj = j // m
            yj = j % m
            if l[xj][yj] == 0:
                for k in range(j + 1, n * m):
                    temp = [item[:] for item in l]
                    temp[xi][yi] = 1
                    temp[xj][yj] = 1
                    xk = k // m
                    yk = k % m
                    if l[xk][yk] == 0:
                        temp[xk][yk] = 1
                    for x, y in l2:
                        bfs(x,y)
                    tempR = 0
                    for a in range(n * m):
                        xa = a // m
                        ya = a % m
                        if temp[xa][ya] == 0:
                            tempR += 1
                    if tempR > result:
                        result = tempR
print(result)
'''
l0 = []
l2 = []
for i in range(n):
    for j in range(m):
        if l[i][j] == 0:
            l0.append((i,j))
        elif l[i][j] == 2:
            l2.append((i,j))

result = 0
for i in range(len(l0)):
    for j in range(len(l0) - i - 1):
        for k in range(len(l0) - j - 1):
            temp = copy.deepcopy(l)
            temp[l0[i][0]][l0[i][1]] = 1
            temp[l0[j+i][0]][l0[j+i][1]] = 1
            temp[l0[k+j][0]][l0[k+j][1]] = 1

            for x, y in l2:
                bfs(x, y)
            tempR = 0
            for a in range(n):
                for b in range(m):
                    if temp[a][b] == 0:
                        tempR += 1
            if result < tempR:
                result = tempR
print(result)
'''