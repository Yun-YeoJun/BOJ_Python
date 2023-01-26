import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

lines = sys.stdin.readlines()

pre_ord = []
n = 0
for line in lines:
    pre_ord.append(int(line))
    n += 1


def post_ord(start,end):
    if start > end:
        return
    mid = end + 1
    for i in range(start + 1, end + 1):
        if pre_ord[i] > pre_ord[start]:
            mid = i
            break
    post_ord(start + 1,mid-1)
    post_ord(mid,end)
    print(pre_ord[start])

post_ord(0,n - 1)