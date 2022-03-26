from sys import stdin

n = int(stdin.readline())
l = []

for i in range(n):
    l.append(int(stdin.readline()))

l.sort(reverse=True)

result = 0

for i in range(n):
    temp = l[i] - i
    if temp <= 0:
        continue
    result += temp

print(result)