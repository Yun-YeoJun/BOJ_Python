from sys import stdin 

l = stdin.readline().rstrip()
result = 0

l = l.replace('c=', '!')
l = l.replace('c-', '!')
l = l.replace('dz=', '!')
l = l.replace('d-', '!')
l = l.replace('lj', '!')
l = l.replace('nj', '!')
l = l.replace('s=', '!')
l = l.replace('z=', '!')

print(len(l))