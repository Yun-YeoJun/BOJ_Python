#bj18111.py

from sys import stdin

n, m, b = map(int, stdin.readline().split())

l = []

for i in range(n):
    temp = list(map(int, stdin.readline().split()))
    for j in temp:
        l.append(j)

l.sort(reverse = True)

time = 1000000000000000000000000000000
resultT = -1
resultH = -1

for i in range(257):
    tempT = 0
    tempB = b
    tf = True
    for j in range(n * m):
        if l[j] > i:
            tempT += 2 * (l[j] - i)
            tempB += 1 * (l[j] - i)
        elif l[j] < i:
            if tempB - 1 * (i-l[j]) >= 0:
                tempT += 1 * (i - l[j])
                tempB -= 1 * (i - l[j])
            else:
                tf = False
                break
    if tf == True:
        if tempT <= time:
            resultT = tempT
            resultH = i
            time = tempT

print(resultT, resultH)

    
    
    
