from sys import stdin

n = int(stdin.readline())

i = 0

l = [-1 for i in range(1000)]

l[0] = 0

while True:
    if l[i + 1] == -1:
        l[i + 1] = (i + 1) * (i + 2) /2
    if l[i] < n <= l[i+1]:
        min = l[i] + 1
        max = l[i+1]
        ea = max - min + 1
        print(int(ea - (n - min)), end =' ')
        print(int(ea - (max - n)))
        break
    i+=1
        
    