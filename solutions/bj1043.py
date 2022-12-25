import sys
input = sys.stdin.readline

def getParent(parent, x):
    if parent[x] == x:
        return x
    else:
        parent[x] = getParent(parent, parent[x])
        return parent[x]
    
def unionParent(parent,a,b):
    a = getParent(parent,a)
    b = getParent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def findParent(parent, a, b):
    a = getParent(parent, a)
    b = getParent(parent, b)
    if a == b:
        return 1
    else:
        return 0


n, m = map(int,input().split())

temp = list(map(int,input().split()))

numOfKnow = temp[0]

if numOfKnow == 0:
    know = []
else:
    know = temp[1:]

parent = [i for i in range(n + 1)]

result = m

ls = [[] for i in range(m)]

for i in range(m):
    ls[i] = list(map(int,input().split()))
    l = ls[i]
    numOfParticipate = l[0]

    for j in l[1:]:
        unionParent(parent,l[1],j)

for i in ls:
    member = i[1]
    for j in know:
        if findParent(parent,j,member):
            result -= 1
            break

print(result)