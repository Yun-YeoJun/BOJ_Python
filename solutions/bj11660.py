# import sys
# input = sys.stdin.readline

# n, m = map(int,input().split())

# l = [[] for j in range(n)]

# part_sum = [[0 for i in range(n)] for j in range(n)]

# for i in range(n):
#     l[i] = list(map(int,input().split()))


# for i in range(n):
#     for j in range(n):
#         if j == 0:
#             part_sum[i][j] = l[i][j]
#         else:
#             part_sum[i][j] = part_sum[i][j - 1] + l[i][j]

# for i in range(m):
#     result = 0
#     x1,y1,x2,y2 = map(int,input().split())
#     for x in range(x1 - 1,x2):
#         if y1 == 1:
#             result += part_sum[x][y2-1]
#         else:
#             result += part_sum[x][y2 - 1] - part_sum[x][y1 - 2]

#     print(result)

import sys
input = sys.stdin.readline

n, m = map(int,input().split())

l = [[] for i in range(n + 1)]

l[0] = [0 for i in range(n)]

for i in range(1,n+1):
    l[i] = [0] + list(map(int,input().split()))

prefix_sum = [[0 for i in range(n + 1)] for j in range(n + 1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        prefix_sum[i][j] = l[i][j] + prefix_sum[i][j - 1] + prefix_sum[i - 1][j] - prefix_sum[i - 1][j - 1]


for i in range(m):
    x1,y1,x2,y2=map(int,input().split())

    print(prefix_sum[x2][y2] - prefix_sum[x1 - 1][y2] - prefix_sum[x2][y1 - 1] + prefix_sum[x1-1][y1-1])

