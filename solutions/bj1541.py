import sys
input = sys.stdin.readline

l = input().split('-')

result = 0

for i in l[0].split('+'):
    result += int(i)

for i in l[1:]:
    for j in i.split('+'):
        result -= int(j)

print(result)