from sys import stdin

n, m = map(int, stdin.readline().split())

l = []

for i in range(n):
    l.append(list(map(int,stdin.readline().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

result = 0

for i in range(n):
    for j in range(m):
        stack = []
        stack.append((i,j,l[i][j],(i,j),1))
        while stack:
            x, y, point, visited, cnt = stack.pop()
            if cnt < 4:
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        continue
                    if (nx,ny) == visited:
                        continue
                    stack.append((nx, ny, l[nx][ny] + point, (x,y), cnt + 1))
                    
            if result < point:
                result = point
        
        if j + 2 < m:
            t = l[i][j] + l[i][j + 1] + l[i][j + 2]
            t1, t2 = 0, 0
            if i - 1 >= 0:
                t1 = l[i - 1][j + 1]
            if i + 1 < n:
                t2 = l[i + 1][j + 1]
            t = t + max(t1,t2)
            if result < t:
                result = t
        
        if i + 2 < n:
            t = l[i][j] + l[i + 1][j] + l[i + 2][j]
            t1,t2 = 0,0
            if j - 1 >= 0:
                t1 = l[i + 1][j - 1]
            if j + 1 < m:
                t2 = l[i + 1][j + 1]
            t = t + max(t1,t2)
            if result < t:
                result = t

print(result)