from sys import stdin

s = 0b00000000000000000000

def add(x):
    global s
    s |= (1 << x - 1)

def remove(x):
    global s
    s = s & (~(1 << x - 1))

def empty():
    global s
    s = 0b00000000000000000000

def all():
    global s
    s = 0b11111111111111111111

def check(x):
    global s
    if s & (1<<x-1) == 0:
        print(0)
    else:
        print(1)

def toggle(x):
    global s
    temp = s
    t = (temp >> (x-1)) & 1
    if t == 1:
        s -= 2 ** (x-1)
    else:
        s += 2 ** (x-1)

m = int(stdin.readline())

for tc in range(m):
    l = stdin.readline().rstrip()
    command = l[:3]
    if command == 'add':
        add(int(l[4:]))
    elif command == 'che':
        check(int(l[6:]))
    elif command == 'rem':
        remove(int(l[6:]))
    elif command == 'tog':
        toggle(int(l[7:]))
    elif command == 'all':
        all()
    elif command == 'emp':
        empty()