import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int,input().split())

#fast_time = math.inf
num_of_methods = 0

visited = [-1 for i in range(100001)]

visited[n] = 0

def bfs(n,k):
    global fast_time
    global num_of_methods
    queue = deque()
    queue.append(n)
    while queue:
        now = queue.popleft()

        #visited[now] = 1

        if now == k:
            num_of_methods += 1

        moves = [now - 1, now + 1, now * 2]

        for i in moves:
            if i < 0 or i > 100000:
                continue
            elif visited[i] == -1 or visited[i] >= visited[now] + 1:
                visited[i] = visited[now] + 1
                queue.append(i)
            # visited[i] = 1
            #queue.append((i,time+1))

bfs(n,k)

print(visited[k])
print(num_of_methods)