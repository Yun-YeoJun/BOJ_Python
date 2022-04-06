from sys import stdin
from collections import deque

a, b = map(int, stdin.readline().split())
queue = deque()
queue.append((a, 0))
result = -1
while queue:
    n, cnt = queue.popleft()
    if n == b:
        result = cnt + 1
        break
    n2 = 2 * n
    n1 = n * 10 + 1

    if n2 <= b:
        queue.append((n2, cnt+1))
    if n1 <= b:
        queue.append((n1, cnt+1))
print(result)