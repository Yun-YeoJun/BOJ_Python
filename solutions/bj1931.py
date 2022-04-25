from sys import stdin

n = int(stdin.readline())

l = []

for i in range(n):
    t1, t2 = map(int, stdin.readline().split())
    t3 = abs(t1-t2)
    l.append([t1,t2,t3])



l.sort(key = lambda x:(x[0],x[2]))

result = 0

print(l)