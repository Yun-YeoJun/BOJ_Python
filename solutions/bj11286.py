from sys import stdin
import heapq

n = int(stdin.readline())
heap = []

for i in range(n):
    x = int(stdin.readline())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap,(abs(x),x))

