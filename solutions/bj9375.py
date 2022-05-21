from sys import stdin

t = int(stdin.readline())

for _ in range(t):
    n = int(stdin.readline())
    dic = {}
    for i in range(n):
        a,b = stdin.readline().rstrip().split()
        if b in dic:
            dic[b] += 1
        else:
            dic[b] = 2
    result = 1
    for i in list(dic.values()):
        result *= i
    print(result-1)