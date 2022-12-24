import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    result_max = 0
    n = int(input())
    l = []
    l.append(list(map(int,input().split())))
    l.append(list(map(int,input().split())))

    if n == 1:
        print(max(l[0][0],l[1][0]))
        continue

    result = [[0 for i in range(n)] for j in range(2)]

    result[0][0] = l[0][0]
    result[1][0] = l[1][0]

    result[0][1] = result[1][0] + l[0][1]
    result[1][1] = result[0][0] + l[1][1]

    for i in range(2,n):
        result[0][i] = max(result[1][i-1],result[1][i-2]) + l[0][i]
        result[1][i] = max(result[0][i-1],result[0][i-2]) + l[1][i]


    print(max(result[0][n-1],result[1][n-1]))