from sys import stdin

n = int(stdin.readline())

l =[[0, 0, 0] for i in range(n)]

i = 0
while i < n:
    temp = list(stdin.readline().split())
    l[i][0] = int(temp[0])
    l[i][1] = temp[1]
   # l[i][2] = temp[1]
    i+=1

l.sort()

for i in l:
    print("%d %s" %(i[0], i[1]))
    
