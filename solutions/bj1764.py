from sys import stdin

n, m = map(int, stdin.readline().split())

hl = {}
result = []

for i in range(n):
    hl[stdin.readline().rstrip()] = 1

for i in range(m):
    t = stdin.readline().rstrip()
    if t in hl:
        result.append(t)
    
print(len(result))

result = sorted(result)

for i in result:
    print(i)