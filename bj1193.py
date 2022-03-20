from sys import stdin

x = int(stdin.readline())

l = 1
n = 1

while x > l:
    n += 1
    l = n * (n + 1) // 2

if n % 2 == 0:
    numerator = n - (l - x) #분자
    n -= 1
    l = n * (n + 1) // 2 + 1
    n += 1
    denominator = n - (x - l) #분모
else:
    denominator = n - (l - x) #분모
    n -= 1
    l = n * (n + 1) // 2 + 1
    n += 1
    numerator = n - (x - l) #분자

print("%d/%d" %(numerator, denominator))