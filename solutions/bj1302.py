from sys import stdin

n = int(stdin.readline())

d = {}

for i in range(n):
    temp = stdin.readline().rstrip()

    if temp in d:
        d[temp] += 1
    else:
        d[temp] = 1

l = list(d.keys())
v = list(d.values())

v = sorted(v)

rnum = v[len(v) - 1]

ll = []

for i in l:
    if d[i] == rnum:
        ll.append(i)
ll = sorted(ll)

print(ll[0])