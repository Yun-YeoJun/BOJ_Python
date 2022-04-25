from sys import stdin

n = int(stdin.readline())
l = []
i = 1

while i * i <= n:
    l.append(i*i)
    i += 1

result = -1

for i in l:
    if n == i:
        result = 1
        break

if result == -1:
    for i in l:
        for j in l:
            if n == i + j:
                result = 2
                break
        if result == 2:
            break

if result == -1:
    for i in l:
        for j in l:
            for k in l:
                if n == i + j + k:
                    result = 3
                    break
            if result == 3:
                break
        if result == 3:
            break

if result == -1:
    result = 4

print(result)