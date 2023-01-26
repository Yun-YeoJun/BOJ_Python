import sys
input = sys.stdin.readline

n = int(input())

l = [list(map(int,input().split())) for i in range(n)]

horizontal = [[0 for i in range(n)] for j in range(n)] # 가로
vertical = [[0 for i in range(n)] for j in range(n)] # 세로
diagonal = [[0 for i in range(n)] for j in range(n)] # 대각선

horizontal[0][1] = 1

for i in range(n):
    for j in range(2,n):
        if l[i][j] == 1:
            continue

        if j - 1 >= 0:
            horizontal[i][j] += horizontal[i][j - 1]
            horizontal[i][j] += diagonal[i][j - 1]

        if i - 1 >= 0:
            vertical[i][j] += vertical[i - 1][j]
            vertical[i][j] += diagonal[i - 1][j]

        if i - 1 >= 0 and j - 1 >= 0:
            if l[i - 1][j] == 0 and l[i][j - 1] == 0:
                diagonal[i][j] += horizontal[i - 1][j - 1]
                diagonal[i][j] += vertical[i - 1][j - 1]
                diagonal[i][j] += diagonal[i - 1][j - 1]

print(horizontal[n - 1][n - 1] + vertical[n - 1][n - 1] + diagonal[n - 1][n - 1])
