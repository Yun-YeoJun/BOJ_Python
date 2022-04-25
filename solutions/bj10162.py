from sys import stdin

t = int(stdin.readline())

r1 = t // 300
t %= 300

r2 = t // 60
t %= 60

r3 = t // 10
t %= 10

if t != 0:
    print(-1)
else:
    print(r1,r2,r3)