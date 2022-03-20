from sys import stdin

n = int(stdin.readline())

result = 0

for i in range(1, n + 1):
    i = list(str(i))
    if len(i) == 1:
        result += 1
        continue
    d = int(i[1]) - int(i[0])
    tf = True

    for j in range(len(i) - 1):
        if int(i[j + 1]) - int(i[j]) != d:
            tf = False
            continue
    if tf == True:
        result += 1
print(result)