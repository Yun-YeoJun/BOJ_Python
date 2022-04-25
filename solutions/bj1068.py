from sys import stdin
from collections import deque

n = int(stdin.readline())

tree = {}

inputList = list(map(int, stdin.readline().rstrip().split()))

for i in range(n):
    tree[i] = inputList[i]

queue = deque()

delNode = int(stdin.readline())

del tree[delNode]

for i in tree.copy().keys():
    if tree[i] == delNode:
        queue.append(i)
        del tree[i]

while queue:
    delNode = queue.popleft()
    for i in tree.copy().keys():
        if tree[i] == delNode:
            queue.append(i)
            del tree[i]

keysOfTree = list(tree.keys())

for i in keysOfTree.copy():
    if tree[i] in keysOfTree:
        del keysOfTree[keysOfTree.index(tree[i])]

print(len(keysOfTree))