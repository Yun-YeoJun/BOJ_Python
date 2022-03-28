from sys import stdin

n = int(stdin.readline())

r = n // 3

l = [0] * (int(n**(1/3)) + 1)

l[0] = '*'

for i in range(int(n**(1/3))):
    temp = [' '*(3**i)]*(3**i)
    #tl = l[i] + temp + l[i]
    l[i + 1] = []
    l[i + 1].append(l[i] + l[i] + l[i])
    l[i + 1].append(-1)
    l[i + 1][1] = []
    for j in l[i]:
        l[i + 1][1].append(j)
    for j in temp:
        l[i + 1][1].append(j)
    for j in l[i]:
        l[i + 1][1].append(j)
    l[i + 1].append(l[i]+l[i]+l[i])

#for i in range()

print(l)