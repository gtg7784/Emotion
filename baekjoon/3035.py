a, b, d, c = input().split()
a, b, c, d = int(a), int(b), int(c), int(d)
e = []

for i in range(a):
    z = input()
    e.append(z)

for i in range(a):
    for k in range(d):
        for j in range(b):
            print(e[i][j:j+1]*c, end='')
        print('')