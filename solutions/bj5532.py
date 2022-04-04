from sys import stdin
import math

l = int(stdin.readline()) # day
a = int(stdin.readline()) # page number of korean
b = int(stdin.readline()) # page number of math
c = int(stdin.readline()) # max page of korean
d = int(stdin.readline()) # max page of math

temp1 = math.ceil(a / c)
temp2 = math.ceil(b / d)

result = l - max(temp1, temp2)

print(result)