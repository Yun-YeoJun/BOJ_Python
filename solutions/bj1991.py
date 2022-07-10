import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

graph = {}

for i in range(n):
    a,b,c = input().split()
    graph[a] = [b,c]

def preorder(root):
    if root != '.':
        print(root,end='')
        preorder(graph[root][0])
        preorder(graph[root][1])

def inorder(root):
    if root != '.':
        inorder(graph[root][0])
        print(root,end='')
        inorder(graph[root][1])

def postorder(root):
    if root != '.':
        postorder(graph[root][0])
        postorder(graph[root][1])
        print(root,end='')


preorder('A')
print()

inorder('A')
print()

postorder('A')
print()