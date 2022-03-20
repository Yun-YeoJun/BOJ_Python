from sys import stdin 

n = int(stdin.readline())

a = list(map(int, stdin.readline().rstrip().split()))
b = list(map(int, stdin.readline().rstrip().split()))

a.sort()
b.sort(reverse = True)

result = 0

for i in range(n):
    result += a[i] * b[i]

print(result)