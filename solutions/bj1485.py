from sys import stdin

t = int(stdin.readline())

for i in range(t):
    l = list(range(4))
    for j in range(4):
        l[j] = list(map(int, stdin.readline().split()))
    l.sort()

    l1 = ((l[0][0] - l[1][0])**2 + (l[0][1] - l[1][1])**2)**0.5
    l2 = ((l[0][0] - l[2][0])**2 + (l[0][1] - l[2][1])**2)**0.5
    l3 = ((l[3][0] - l[1][0])**2 + (l[3][1] - l[1][1])**2)**0.5
    l4 = ((l[3][0] - l[2][0])**2 + (l[3][1] - l[2][1])**2)**0.5

    if l1 == l2 and l1 == l3 and l1 == l4 and l2 == l3 and l2 == l4 and l3 == l4:
        if ((l[1][0] - l[2][0])**2 + (l[1][1] - l[2][1])**2)**0.5 == ((l[3][0] - l[0][0])**2 + (l[3][1] - l[0][1])**2)**0.5
            print('1')
        else:
            print('0')
    else:
        print('0')

