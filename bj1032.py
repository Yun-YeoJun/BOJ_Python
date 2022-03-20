from sys import stdin

n = int(stdin.readline())

l = []

for i in range(n):
    l.append(stdin.readline().rstrip())

result = l[0]

for i in l:
    for j in range(len(l[0])):
        if result[j] != i[j]:
            temp = list(result)
            temp[j] = '?'
            result = ''.join(temp)
print(result)
