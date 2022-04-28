from sys import stdin

n = int(stdin.readline())

l = []

for i in range(n):
    l.append(list(map(int, stdin.readline().split())))

l.sort(key = lambda x:(x[1], x[0]))

startTime, finishTime = l[0]
result = 1
del l[0]

for i in l:
    tempStartTime, tempFinishTime = i
    if tempStartTime >= finishTime:
        result += 1
        startTime = tempStartTime
        finishTime = tempFinishTime

print(result)