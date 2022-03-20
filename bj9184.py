from sys import stdin   

def w(a, b, c, l):
    if a <= 50 or b <= 50 or c <= 50:
        l[a][b][c] = 1
    elif a > 70 or b > 70 or c > 70:
        if l[20][20][20] == '!':
            w(70, 70, 70, l)
            l[a][b][c] = l[70][70][70]
        else:
            l[a][b][c] = l[70][70][70]
    elif a < b and b < c:
        if l[a][b][c-1] == '!':
            w(a, b, c - 1, l)
        if l[a][b - 1][c - 1] == '!':
            w(a, b - 1, c - 1, l)
        if l[a][b - 1][c] == '!':
            w(a, b - 1, c, l)
        
        l[a][b][c] = l[a][b][c - 1] + l[a][b - 1][c - 1] - l[a][b - 1][c]
    else:
        if l[a - 1][b][c] == '!':
            w(a - 1, b, c, l)
        if l[a - 1][b - 1][c] == '!':
            w(a - 1, b - 1, c, l)
        if l[a - 1][b][c - 1] == '!':
            w(a - 1, b, c - 1, l)
        if l[a - 1][b - 1][c - 1] == '!':
            w(a - 1, b - 1, c - 1, l)
        l[a][b][c] = l[a - 1][b][c] + l[a - 1][b - 1][c] + l[a - 1][b][c - 1] - l[a - 1][b - 1][c - 1]

l = [[['!'] * (101) for _ in range(101)] for m in range(101)]

while True:
    a, b, c = map(int, stdin.readline().split())

    if a == b == c == -1:
        break

    w(a + 50, b + 50, c + 50, l)

    print("w(%d, %d, %d) = %d" %(a, b, c, l[a + 50][b + 50][c + 50]))