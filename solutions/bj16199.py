by, bm, bd = map(int,input().split())
sy, sm, sd = map(int,input().split())

y3 = sy - by
y2 = y3 + 1
y1 = 0

if bm > sm:
    y1 = sy - by - 1
elif bm == sm:
    if bd > sd:
        y1 = sy - by - 1
    else:
        y1 = sy - by
else:
    y1 = sy - by

print(y1)
print(y2)
print(y3)
