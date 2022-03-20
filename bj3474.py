from sys import stdin
import math

t = int(stdin.readline())

i = 0
while i < t:
    n = int(stdin.readline())
    n = math.factorial(n)
    result = 1
    while True:
        if n % (10 ** result) != 0:
            print(result - 1)
            break
        else:
            result += 1
    
    i += 1
