import sys
from collections import deque
input = sys.stdin.readline

def bfs(x,n):
    queue = deque()
    queue.append(x)
    time = delay[x - 1]
    visited = [0 for i in range(n + 1)]

    while queue:
        cur = queue.popleft()
        temp = (0,-1)

        if cur not in graph:
            #time += delay[cur]
            continue

        for i in graph[cur]:
            #temp = max(temp,delay[i - 1])

            temp_time, temp_position = temp

            if temp_time < delay[i - 1]

            queue.append(i)
        time += temp

    return time

t = int(input())

for _ in range(t):
    n,k = map(int,input().split())

    delay = list(map(int,input().split()))

    graph = {}

    for i in range(k):
        x,y = map(int,input().split())

        if y not in graph:
            graph[y] = [x]
        else:
            graph[y].append(x)

    w = int(input())

    print(bfs(w,n))

    