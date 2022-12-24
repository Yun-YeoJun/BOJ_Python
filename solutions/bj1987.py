import sys
input = sys.stdin.readline

r,c=map(int,input().split())

# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

l = [[] for i in range(r)]

for i in range(r):
    l[i] = list(input())

print(l)