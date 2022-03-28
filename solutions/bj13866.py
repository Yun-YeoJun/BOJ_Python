from sys import stdin

l = list(map(int, stdin.readline().rstrip().split()))

l = sorted(l)

r = abs((l[0] + l[3]) - (l[1] + l[2]))

print(r)