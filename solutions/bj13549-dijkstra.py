import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n,k=map(int,input().split())

distance = [INF] * (100001)
graph = [[] for i in range(100001)]

for i in range(100001):
    if i * 2 <= 100000:
        graph[i] = [(i * 2, 0),(i - 1, 1),(i + 1,1)]
    elif i + 1 <= 100000:
        graph[i] = [(i - 1, 1), (i + 1, 1)]
    else:
        graph[i] = [(i - 1, 1)]

q = []
heapq.heappush(q,(0,n))
distance[n] = 0
while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for i in graph[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q,(cost,i[0]))

print(distance[k])