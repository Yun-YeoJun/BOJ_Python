from sys import stdin
l = stdin.readline()

col = l.count('[') - 1  #세로

temp = 0

for i in ['0', '1']:
    temp += l.count(i)
    
row = temp // col; #가로

print(col, row)
