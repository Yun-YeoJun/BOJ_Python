#bj1654.py

from sys import stdin

k, n = map(int, stdin.readline().split())

l = list(range(k))

for i in range(k):
    l[i] = int(stdin.readline())

l.sort() 

start = 1
end = l[k - 1]
result = -1

while start <= end:
    mid = (start + end) // 2
    temp = 0

    for i in l:
        temp += i // mid

    if temp >= n:
        if result < mid:
            result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
    


