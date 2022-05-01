from sys import stdin
from collections import deque

n = int(stdin.readline())

def oneTwoThree(x):
    result = 0
    queue = deque()
    queue.append(x)
    while queue:
        x = queue.popleft()
        t1 = x - 1
        t2 = x - 2
        t3 = x - 3
        if t1 == 0:
            result += 1
        elif t1 > 0:
            queue.append(t1)
        if t2 == 0:
            result += 1
        elif t2 > 0:
            queue.append(t2)
        if t3 == 0:
            result += 1
        elif t3 > 0:
            queue.append(t3)
    return result

for i in range(n):
    print(oneTwoThree(int(stdin.readline())))