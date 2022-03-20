from sys import stdin

n, m = map(int, stdin.readline().split())

HeightList = list(map(int, stdin.readline().split()))
HeightList = sorted(HeightList)

start = 0
end = HeightList[n - 1]

while start <= end:
    mid = (start + end) // 2

    s = 0
    for i in reversed(HeightList):
        if i - mid > 0:
            s += i - mid
        else:
            break

    
    if s >= m:
        start = mid + 1
    elif s < m:
        end = mid - 1

print(end)

