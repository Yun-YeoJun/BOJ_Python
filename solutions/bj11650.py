n = int(input())

l = list(range(n))

i = 0
while i < n:
    l[i] = list(range(2))
    l[i][0], l[i][1] = map(int,input().split())
    i += 1

sl = sorted(l)

for i in sl:
    print("%d %d" %(i[0], i[1]))

