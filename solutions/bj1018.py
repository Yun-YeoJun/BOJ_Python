from sys import stdin
n, m = map(int,stdin.readline().split())

l = list(range(n))

i = 0
while i < n:
    l[i] = list(range(m))
    temp = stdin.readline()
    j = 0
    while j < m:
        if temp[j] == 'W':
            l[i][j] = 0 #흰색(W) == 0
        else:
            l[i][j] = 1 #검은색(B) == 1
        j += 1
    i+=1

result = 10000

x = 0
y = 0
i = 0
j = 0

while y <= n-8:
    x = 0
    while x<= m-8:
        temp1 = 0 #case1 기준점:W
        ptr = 0
        i = 0
        j = 0
        while i < 8:
            j = 0
            while j < 8:
                if ptr == 0:
                    if l[y + i][x + j] == 1:
                        temp1 += 1
                    ptr = 1
                elif ptr == 1:
                    if l[y+i][x+j] == 0:
                        temp1+=1
                    ptr = 0
                j+=1
            if ptr == 0:
                ptr = 1
            elif ptr == 1:
                ptr = 0
            i+=1
            
        temp2 = 0 #case2 기준점:B
        ptr = 1
        i = 0
        j = 0
        while i < 8:
            j = 0
            while j < 8:
                if ptr == 0:
                    if l[y + i][x + j] == 1:
                        temp2 += 1
                    ptr = 1
                elif ptr == 1:
                    if l[y+i][x+j] == 0:
                        temp2+=1
                    ptr = 0
                j+=1
            if ptr == 0:
                ptr = 1
            elif ptr == 1:
                ptr = 0
            i+=1
        if temp1 < result:
            result = temp1
        if temp2 < result:
            result = temp2
        x += 1
    y+=1

print(result)
