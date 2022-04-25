from sys import stdin

l1 = list(map(int, stdin.readline().split()))
l2 = list(map(int, stdin.readline().split()))

print(max(sum(l1), sum(l2)))