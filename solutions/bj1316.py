from sys import stdin 

n = int(stdin.readline())
result = 0

for i in range(n):
    a = [0 for _ in range(26)]
    l = stdin.readline().rstrip()
    l = list(l)
    tf = True

    for j in range(len(l)):
        if j == len(l) - 1:
            c = ord(l[j]) - 97
            if a[c] == 0:
                a[c] += 1
            else:
                tf = False
                continue

        elif j < len(l) - 1:
            if l[j] != l[j + 1]:
                c = ord(l[j]) - 97
                if a[c] == 0:
                    a[c] += 1
                else:
                    tf = False
                    continue
    if tf == True:
        result += 1
print(result)