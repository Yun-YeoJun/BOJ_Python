from sys import stdin

a = int(stdin.readline())
b = int(stdin.readline())
c = int(stdin.readline())
d = int(stdin.readline())
p = int(stdin.readline())

def X(a,p):
    return p * a
def Y(b,c,d,p):
    if p <= c:
        return b
    else:
        return b + (p-c)*d

print(min(X(a,p), Y(b,c,d,p)))