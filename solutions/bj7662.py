import sys
import heapq
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    minHeap = []
    maxHeap = []
    k = int(input())
    id = 0
    visited = [False] * 1000001
    for i in range(k):
        cmd = input().rstrip()
        if cmd[0] == "I":
            heapq.heappush(minHeap,(int(cmd[2:]),id))
            heapq.heappush(maxHeap,(-int(cmd[2:]),int(cmd[2:]),id))
            visited[id] = True 
            id += 1
        else:
            if cmd[2:] == '-1':
                while minHeap and not visited[minHeap[0][1]]:
                    heapq.heappop(minHeap)
                if minHeap:
                    visited[minHeap[0][1]] = False
                    heapq.heappop(minHeap)
            else:
                while maxHeap and not visited[maxHeap[0][2]]:
                    heapq.heappop(maxHeap)
                if maxHeap:
                    visited[maxHeap[0][2]] = False
                    heapq.heappop(maxHeap)
            id += 1

    while minHeap and not visited[minHeap[0][1]]:
        heapq.heappop(minHeap)
    while maxHeap and not visited[maxHeap[0][2]]:
        heapq.heappop(maxHeap)
    if len(minHeap) == 0 or len(maxHeap) == 0:
        print("EMPTY")
    else:
        print(maxHeap[0][1],minHeap[0][0])