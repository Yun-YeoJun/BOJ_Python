from sys import stdin

while True:
    n = int(stdin.readline())

    if n == 0:
        break

    l = [0 for _ in range(n)]
    l2 = [0 for _ in range(n)]

    for i in range(n):
        l[i] = stdin.readline().rstrip()
        l2[i] = l[i].lower()
    
    l2.sort()

    for i in l:
        if i.lower() == l2[0]:
            print(i)
            break
