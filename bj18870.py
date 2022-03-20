from sys import stdin  

n = int(stdin.readline())

l = list(map(int, stdin.readline().rstrip().split()))

s = list(set(l))

s.sort()

d = {}

for i in range(len(s)):
    d[s[i]] = i

print(' '.join([str(d[i]) for i in l]))