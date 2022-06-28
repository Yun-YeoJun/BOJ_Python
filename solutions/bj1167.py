import sys
from collections import deque
input = sys.stdin.readline

v = int(input())

graph = {}

for i in range(1,v+1):
    graph[i] = []

for i in range(v):
    l = list(map(int,input().split()))
    node = l[0]
    for j in range((len(l) - 2) // 2):
        dest = l[j * 2 + 1]
        length = l[j * 2 + 2]
        graph[node].append((dest,length))
        graph[dest].append((node,length))

def dfs(x):
    global v
    stack = deque()
    stack.append((x,0))
    result = [1,0]
    visited = [0 for i in range(v + 1)]
    visited[x] = 1
    while stack:
        n,l = stack.pop()
        for i in graph[n]:
            if visited[i[0]] == 0:
                visited[i[0]] = 1
                stack.append((i[0],l+i[1]))
                if result[1] < l + i[1]:
                    result = [i[0],l+i[1]]
    return result

re = dfs(1)
print(dfs(re[0])[1])