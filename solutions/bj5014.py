from sys import stdin
from collections import deque

# 건물의 총 층수 : f, 스타트링크의 층수 : g, 현재 위치 : s, 엘리베이터 위 아래 층수: u, d
f, s, g, u, d = map(int, stdin.readline().split())

queue = deque()

queue.append((s, 0))
visited = [0 for _ in range(f + 1)]

result = -1

while queue:
    floor, cnt = queue.popleft()

    if floor == g:
        result = cnt
        break

    if visited[floor] != 0:
        continue
    else:
        visited[floor] += 1
    
    upFloor = floor + u
    downFloor = floor - d

    if upFloor <= f and upFloor > 0:
        queue.append((upFloor, cnt+1))
    if downFloor <= f and downFloor > 0:
        queue.append((downFloor, cnt + 1))

if result == -1:
    print("use the stairs")
else:
    print(result)