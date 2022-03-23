from sys import stdin

n = int(stdin.readline())

l = [0] * n

for i in range(n):
    l[i] = int(stdin.readline())

l = sorted(l)

temp = l[:]

result = 0

while len(temp) > 2:
    l = temp[:]

    temp = [0] * (len(l) - 1)

    temp[0] = l[0] + l[1]
    result += temp[0]

    for i in range(1, len(l) - 1):
        temp[i] = l[i + 1]

    temp = sorted(temp)


result += temp[0] + temp[1]

print(result)