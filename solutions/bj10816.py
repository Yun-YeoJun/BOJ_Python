from sys import stdin
n = int(stdin.readline())
l = list(map(int, stdin.readline().split()))
m = int(stdin.readline())
checkList = list(map(int, stdin.readline().split()))

l = sorted(l)

def lowerBound(target, data):
    low = 0
    high = len(data)
    mid = 0
    while low < high:
        mid = (low + high) // 2
        if target <= data[mid]:
            high = mid
        else:
            low = mid + 1
    return low

def upperBound(target, data):
    low = 0
    high = len(data)
    mid = 0
    while low < high:
        mid = (low + high) // 2
        if target >= data[mid]:
            low = mid + 1
        else:
            high = mid
    return low

for i in checkList:
    lowIdx = lowerBound(i, l)
    upIdx = upperBound(i, l)

    print("%d " %(upIdx - lowIdx), end = '')

print()


