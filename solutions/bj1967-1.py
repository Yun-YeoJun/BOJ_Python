from sys import stdin
from collections import deque
n = int(stdin.readline())
l = {}

for i in range(1, n + 1):
    l[i] = []

for i in range(n - 1):
    a, b, c = map(int, stdin.readline().split())
    l[a].append((b,c))

def dfs(x):
    child = []

    for i in l[x]:
        child.append(i)

    if len(child) == 0:
        return 0

    result = [0 for i in range(len(child))]

    j = 0
    for idx, length in child:
        stack = deque()
        stack.append((idx, length))
        while stack:
            idx, length = stack.pop()
            leaf = True

            for i in l[idx]:
                leaf = False
                stack.append((i[0], length + i[1]))

            if leaf == True:
                result[j] = max(result[j], length)
        j+=1
        
    result = sorted(result)
    r = 0
    if len(child) == 1:
        r = result[len(result) - 1]
    else:
        for i in range(1,3):
            r += result[len(result) - i]
    return r


result = 0
for i in range(1, n+1):
    result = max(result, dfs(i))
print(result)