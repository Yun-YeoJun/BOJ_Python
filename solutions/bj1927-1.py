from sys import stdin
from collections import deque

n = int(stdin.readline())
heap = deque()
heap.append(-1)

def insert(x):
    heap.append(x)
    idx = len(heap) - 1
    while((idx != 1) and (x < heap[idx // 2])):
        heap[idx], heap[idx//2] = heap[idx//2], heap[idx]
        idx = idx//2

def delete():
    if len(heap) == 1:
        print(0)
        return
    heap.popleft()
    heap[0], heap[len(heap) - 1] = heap[len(heap) - 1], heap[0]
    print(heap.pop())
    heap.appendleft(-1)
    parent = 1
    while True:
        child = parent * 2

        if (child + 1 < len(heap) and heap[child] > heap[child + 1]):
            child += 1
        if (child >= len(heap) or heap[child] > heap[parent]):
            break
        heap[child], heap[parent] = heap[parent], heap[child]
        parent = child

for _ in range(n):
    x = int(stdin.readline())
    if x == 0:
        delete()
    else:
        insert(x)