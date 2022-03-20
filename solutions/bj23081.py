from sys import stdin

def up(l, row, col):
    for c in range(col):
        if l[row][c] == 'B':
            

n = int(stdin.readline())

l = list(range(n))

for i in range(n):
    temp = stdin.readline().rstrip()
    l[i] = list(temp)

print(l)
