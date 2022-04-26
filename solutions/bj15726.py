from sys import stdin
import math

a, b, c = map(int, stdin.readline().split())

r1 = a * b / c
r2 = a / b * c

print(math.trunc(max(r1, r2)))