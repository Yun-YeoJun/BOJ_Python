import sys
input = sys.stdin.readline

n = int(input())

maxList = list(map(int,input().split()))
minList = maxList[:]

d = [-1,0,1]

for i in range(n-1):
    prevMax = maxList[:]
    prevMin = minList[:]

    l = list(map(int,input().split()))

    for j in range(3):
        tempMin = 10 * n
        for k in range(3):
            t = j + d[k]
            if t < 0 or t >= 3:
                continue
            tempMin = min(tempMin,prevMin[t])
            maxList[j] = max(prevMax[t] + l[j], maxList[j])
        minList[j] = l[j] + tempMin

print(max(maxList),end=" ")
print(min(minList))