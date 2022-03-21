from sys import stdin

b = [0 for _ in range(3)]
j = [0 for _ in range(2)]

for i in range(3):
    b[i] = int(stdin.readline())
for i in range(2):
    j[i] = int(stdin.readline())
b.sort()
j.sort()

result = b[0] + j[0] - 50

print(result)