from sys import stdin
from collections import deque

n, k = map(int, stdin.readline().split())
max = 100000
visited = [0 for i in range(max + 1)]

def bfs(n):
    global k
    queue = deque()
    visited[n] = 1
    queue.append((n, 0))
    while queue:
        x, sec = queue.popleft()
        if x > max:
            continue
        if x < 0:
            continue
        if x == k:
           print(sec)
           break
        if 0 <= x - 1 <= max and not visited[x-1] == 1: 
            queue.append((x-1, sec+1))
            visited[x-1] = 1
        if 0 <= x + 1 <= max and not visited[x+1] == 1:
            queue.append((x+1,sec+1))
            visited[x+1] = 1
        if 0 <= 2 * x <= max and not visited[2 * x] == 1:
            queue.append((2*x,sec+1))
            visited[2*x] = 1

bfs(n)