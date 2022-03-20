from sys import stdin   

n = int(stdin.readline())

m = n % 2

for i in range(n // 2):
    print('1 2', end = ' ')

if m == 1:
    print('3', end = '')
print()