from sys import stdin

n, m = map(int, stdin.readline().split())

l = []

for i in range(n):
    l.append(list(map(int,stdin.readline().split())))

def tetromino1(x,y):
    t1 = 0
    t2 = 0
    for i in range(4):
        if 0 <= x + i < n:
            t1 += l[x+i][y]
        if 0 <= y + i < m:
            t2 += l[x][y+i]
    return max(t1,t2)

def tetromino2(x,y):
    if 0 <= x + 1 < n:
        if 0 <= y + 1 < m:
            return l[x][y] + l[x + 1][y] + l[x][y + 1] + l[x + 1][y + 1]
        else:
            return 0
    else:
        return 0

def tetromino3(x,y):
    if 0 <= x + 2 < n:
        t = l[x][y] + l[x + 1][y] + l[x + 2][y]
        t1,t2,t3,t4 = 0,0,0,0
        if 0<=y-1<m:
            t1 = l[x][y - 1]
            t3 = l[x + 2][y - 1]
        if 0<=y+1<m:
            t2 = l[x][y + 1]
            t4 = l[x + 2][y + 1]

        return t + max(t1,t2,t3,t4)
    else:
        return 0

def tetromino4(x, y):
    if 0 <= y + 2 < m:
        t = l[x][y] + l[x][y + 1] + l[x][y + 2]
        t1,t2,t3,t4 = 0,0,0,0
        if 0<=x-1<n:
            t1 = l[x - 1][y]
            t3 = l[x - 1][y + 2]
        if 0<=x+1<n:
            t2 = l[x + 1][y]
            t4 = l[x + 1][y + 2]

        return t + max(t1,t2,t3,t4)
    else:
        return 0

def tetromino5(x,y):
    if 0 <= y + 1 < m:
        if 0 <= x - 1 < n and 0 <= x + 1 < n:
            t = l[x][y] + l[x][y + 1]
            t1 = l[x - 1][y] + l[x + 1][y + 1]
            t2 = l[x - 1][y + 1] + l[x + 1][y]
            return t + max(t1,t2)
        else:
            return 0
    else:
        return 0

def tetromino6(x,y):
    if 0 <= x + 1 < n:
        if 0 <= y - 1 < m and 0 <= y + 1 < m:
            t = l[x][y] + l[x + 1][y]
            t1 = l[x][y - 1] + l[x + 1][y + 1]
            t2 = l[x][y + 1] + l[x + 1][y - 1]
            return t + max(t1,t2)
        else:
            return 0
    else:
        return 0

def tetromino7(x,y):
    if 0 <= y + 2 < m:
        t = l[x][y] + l[x][y + 1] + l[x][y + 2]
        t1,t2 = 0,0
        if 0 <= x - 1 < n:
            t1 = l[x - 1][y + 1]
        if 0 <= x + 1 < n:
            t2 = l[x + 1][y + 1]
        return t + max(t1,t2)
    else:
        return 0

def tetromino8(x,y):
    if 0 <= x + 2 < n:
        t = l[x][y] + l[x + 1][y] + l[x + 2][y]
        t1,t2 = 0,0
        if 0 <= y - 1 < m:
            t1 = l[x + 1][y - 1]
        if 0 <= y + 1 < m:
            t2 = l[x + 1][y + 1]
        return t + max(t1,t2)
    else:
        return 0

result = 0

for x in range(n):
    for y in range(m):
        t = max(tetromino1(x,y),tetromino2(x,y),tetromino3(x,y),tetromino4(x,y),tetromino5(x,y),tetromino6(x,y),tetromino7(x,y),tetromino8(x,y),)
        if result < t:
            result = t

print(result)