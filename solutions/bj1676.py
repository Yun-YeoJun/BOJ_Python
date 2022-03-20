def factorial(n):
    if n>1:
        return n * factorial(n-1)
    else:
        return 1
    
n = int(input())
n = factorial(n)
i = 1
while True:
    if n % (10 ** i) != 0:
        print(i-1)
        break
    i+=1
