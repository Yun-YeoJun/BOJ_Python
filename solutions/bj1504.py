import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n,e = map(int,input().split())
graph = [[] for i in range(n + 1)]
for i in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dijkstra(start,n):
    distance = [INF for i in range(n + 1)]
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    return distance

v1, v2 = map(int,input().split())
start_ = dijkstra(1,n)
v1_ = dijkstra(v1,n)
v2_ = dijkstra(v2,n)

result = min(start_[v1] + v1_[v2] + v2_[n], start_[v2] + v2_[v1] + v1_[n])

print(result if result < INF else -1)