from sys import stdin

dic = {}

for i in range(97, 123):
    dic[chr(i)] = i - 96

r = 31
m = 1234567891

l = int(stdin.readline())
c = stdin.readline()

h = 0

i = 0
while i < l:
    h += dic[c[i]] * (r ** i)
    i += 1

h %= m

print(h)
