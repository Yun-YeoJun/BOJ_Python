import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

distance = [[INF for i in range(n + 1)] for j in range(n + 1)]

for i in range(1,n+1):
    distance[i][i] = 0

for i in range(m):
    a,b,c = map(int,input().split())
    if distance[a][b] == INF:
        distance[a][b] = c
    else:
        distance[a][b] = min(c, distance[a][b])

for i in range(1,n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            distance[j][k] = min(distance[j][k],distance[j][i] + distance[i][k])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if distance[i][j] != INF:
            print(distance[i][j],end = ' ')
        else:
            print(0,end=' ')
    print()