from sys import stdin 

n, m = map(int, stdin.readline().split())
l = []
for i in range(n):
    l.append(stdin.readline().rstrip())
for i in range(m):
    s = stdin.readline().rstrip()
    if s.isalpha():
        print(l.index(s) + 1)
    else:
        print(l[int(s) - 1])