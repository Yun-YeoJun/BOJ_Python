from sys import stdin
from collections import deque

n = int(stdin.readline())

que = deque()

i = 1
while i <= n:
    que.append(i)
    i+=1

while True:
    if len(que) == 1:
        print("%d" %que.popleft())
        break
    que.popleft()
    que.append(que.popleft())

