import sys
arr = list(map(int, sys.stdin.readline().rstrip().split()))
a = arr[0]
b = arr[1]

if a == 0:
    print("0\n0")
elif a < 0 and b < 0:
    print("%d\n%d" %(a // b + 1, 1 - (a%b)))
elif a < 0 or b < 0:
    if b < 0:
        q = 0
        while True:
            if 0 <= a - q*b <= abs(b):
                r = a - q*b
                break
            else:
                q-=1
    else:
        q = 0
        while True:
            if 0<=a-q*b<=b:
                r=a-q*b
                break
            else:
                q-=1
                
    print(q)
    print(r)
    
elif a > 0 and b >0:
    print("%d\n%d" %(a//b, a%b))
