from sys import stdin

a, b = stdin.readline().rstrip().split()

c = len(b) - len(a)

result = -1
temp = 0

for i in range(c + 1):
    temp = 0
    for j in range(len(a)):
        if a[j] != b[j + i]:
            temp += 1
    if result == -1 or result > temp:
        result = temp
print(result)