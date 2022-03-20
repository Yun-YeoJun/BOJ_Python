from sys import stdin

n = int(stdin.readline())
l = []

for i in range(0, n):
    l.append([0,0])

for i in range(0, n):
    l[i][1], l[i][0] = map(int, stdin.readline().split())


l.sort()

for i in range(0, n):
    temp = l[i][1]
    l[i][1] = l[i][0]
    l[i][0] = temp

    print("%d %d" %(l[i][0], l[i][1]))
    
