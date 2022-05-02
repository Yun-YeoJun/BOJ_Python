from sys import stdin
from collections import deque

n = int(stdin.readline())

in_order = list(map(int,stdin.readline().split()))
post_order = list(map(int,stdin.readline().split()))

root = post_order[n - 1]

rootInOrderIdx = in_order.index(root) # rootInOrderIdx를 기준으로 앞 쪽은 left node, 뒷 쪽은 right node
preList = [root]

leftInOrder = in_order[0:rootInOrderIdx]
leftPostOrder = post_order[0:rootInOrderIdx]

rightInOrder = in_order[rootInOrderIdx + 1:]
rightPostOrder = post_order[rootInOrderIdx:n-1]

stack = deque()

stack.append((rightInOrder,rightPostOrder))
stack.append((leftInOrder,leftPostOrder))

while stack:
    InOrder, PostOrder = stack.pop()
    if len(InOrder) == 0 and len(PostOrder) == 0:
        continue
    root = PostOrder[len(PostOrder) - 1]
    rootInOrderIdx = InOrder.index(root)
    preList.append(root)
    leftInOrder = InOrder[0:rootInOrderIdx]
    leftPostOrder = PostOrder[0:rootInOrderIdx]
    rightInOrder = InOrder[rootInOrderIdx + 1:]
    rightPostOrder = PostOrder[rootInOrderIdx:len(PostOrder) - 1]
    stack.append((rightInOrder,rightPostOrder))
    stack.append((leftInOrder,leftPostOrder))

for i in preList:
    print(i, end=' ')
print()