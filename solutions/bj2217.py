from sys import stdin

n = int(stdin.readline())

l = list(range(n))

for i in range(n):
    l[i] = int(stdin.readline())

l = sorted(l)

result = l[0] * n

for i in range(n):
    temp = l[i] * (n - i)
    if temp > result:
        result = temp

print(result)