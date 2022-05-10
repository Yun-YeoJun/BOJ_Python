from sys import stdin

b1 = "0b"+stdin.readline().rstrip()
b2 = "0b"+stdin.readline().rstrip()

result = bin(int(b1,2) * int(b2,2))
print(result[2:])
