from sys import stdin

n = int(stdin.readline())
m = int(stdin.readline())

channel = 100
button = [i for i in range(10)]
delList = []
result = abs(channel - n)
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
        channel = temp
        result = abs(temp - n) + len(str(temp))

print(result)