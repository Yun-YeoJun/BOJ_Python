import sys
input = sys.stdin.readline

m = int(input())

mod = [0 for i in range(m)]
X = 1000000007

result = 0

is_even = lambda x: x % 2 == 0

def calc_pow(n,exp):
    global X
    if exp == 0:
        return 1
    
    if exp == 1:
        return n

    if is_even(exp):
        pow = calc_pow(n, exp // 2)
        return (pow * pow) % X

    else:
        return (calc_pow(n,exp - 1) * n) % X


def calc_inverse_element(n):
    global X

    return calc_pow(n, X - 2) % X

for i in range(m):
    n,s = map(int,input().split())

    n_inverse = calc_inverse_element(n) 

    result += (s * n_inverse) % X
    result %= X

print(result)