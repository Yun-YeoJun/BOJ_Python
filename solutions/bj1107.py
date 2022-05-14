from sys import stdin

n = int(stdin.readline())
m = int(stdin.readline())

button = [i for i in range(10)]
delList = []
result = abs(100 - n)
if m != 0:
    delList = list(map(int,stdin.readline().split()))

for i in delList:
    del button[button.index(i)]

for i in range(1000000):
    iList = list(str(i))
    tf = True
    for j in iList:
        if int(j) in button:
            continue
        tf = False
        break
    if tf == False:
        continue
    temp = i

    if abs(temp - n) + len(str(temp)) < result:
        result = abs(temp - n) + len(str(temp))

print(result)