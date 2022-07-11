import sys
input = sys.stdin.readline

n = int(input())

mr,mg,mb = 0,0,0

for i in range(n):
    r,g,b = map(int,input().split())

    nr = min(r + mg, r + mb)
    ng = min(g + mr, g + mb)
    nb = min(b + mr, b + mg)

    mr = nr
    mg = ng
    mb = nb

print(min(mr,mg,mb))