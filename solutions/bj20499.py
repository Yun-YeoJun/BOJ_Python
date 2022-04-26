from sys import stdin

k, d, a = map(int, stdin.readline().split('/'))

if d == 0 or k + a < d:
    print('hasu')
else:
    print('gosu')