import sys
import math
iput = list(map(int,sys.stdin.readline().rstrip().split()))

m = iput[0]
n = iput[1]

arr = [True for i  in range(n+1)]

for i in range(2, int(math.sqrt(n)) + 1):
    if arr[i] == True:
        j = 2
        while i * j <= n:
            arr[i * j] = False
            j += 1

for i in range(m, n+1):
    if arr[i]:
        print(i)


    
    
