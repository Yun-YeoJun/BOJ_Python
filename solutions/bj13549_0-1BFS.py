import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e9)
n,k=map(int,input().split())

Max = 100000

dist = [INF for i in range(Max + 1)]

dq = deque()

dq.appendleft(n)
dist[n] = 0

while dq:
    cur = dq.popleft()

    if cur == k:
        break

    warp = cur * 2

    if warp <= Max and dist[warp] > dist[cur]:
        dist[warp] = dist[cur]
        dq.appendleft(warp)

    left = cur - 1
    right = cur + 1

    if left >= 0 and dist[left] > dist[cur] + 1:
        dq.append(left)
        dist[left] = dist[cur] + 1
    
    if right <= Max and dist[right] > dist[cur] + 1:
        dq.append(right)
        dist[right] = dist[cur] + 1

print(dist[k])