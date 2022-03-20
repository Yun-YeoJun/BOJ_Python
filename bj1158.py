from sys import stdin

n, k = map(int, stdin.readline().split())

l = list(range(1, n + 1))

cur = 0
result = []

while len(l) > 0:
    cur += k - 1
    if cur > len(l) - 1:
        cur = cur % len(l)
    result.append(l[cur])
    del(l[cur])

print('<', end='')
for i in result:
    if i == result[n - 1]:
        print(i, end = '')
    else:
        print('%d, ' % i, end = '')
print('>')