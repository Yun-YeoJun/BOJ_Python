from sys import stdin 

r = int(stdin.readline())
s = int(stdin.readline())

result = r * 8 + s * 3 -28

if result < 0:
    print(0)
else:
    print(result)