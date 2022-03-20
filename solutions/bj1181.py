n = int(input())
a = []

i = 0
while i < n:
    i += 1
    a.append(input())

l = list(range(50))

i = 0
while i < 50:
    l[i] = list()
    i += 1

for string in a:
    b = len(string)
    l[b - 1].append(string)

i = 0
while i < 50:
    temp = set(l[i])
    l[i] = list(temp)
    i += 1

i = 0
while i < 50:
    length = len(l[i])
    if length == 0:
        i += 1
        continue
    l[i].sort()
    j = 0
    
    while j < length:
        print(l[i][j])
        j += 1
    i += 1


    
