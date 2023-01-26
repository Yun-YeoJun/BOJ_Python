import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

distance = [INF] * (n + 1)
route = [[] for i in range(n + 1)]
graph = [[] for i in range(n + 1)]

for i in range(m):
    a,b,c = map(int,input().split())

    graph[a].append((b,c))

start, end = map(int,input().split())

route[start] = [start]

def dijkstra(start):
    queue = []
    heapq.heappush(queue,(0,start))
    distance[start] = 0

    while queue:
        dist, now = heapq.heappop(queue)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                route[i[0]] = route[now][:]
                route[i[0]].append(i[0])
                heapq.heappush(queue,(cost,i[0]))

dijkstra(start)

print(distance[end])
print(len(route[end]))

for i in route[end]:
    print(i,end=" ")

