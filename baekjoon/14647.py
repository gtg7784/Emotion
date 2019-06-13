a = input().split()
b, c, d, e = [], 0, 0, 0

for i in range(int(a[0])):
    z = input().split()
    b.append(z)


for i in range(len(b)):
    for j in range(len(b[0])):
        e = b[i][j].count('9')
        c += e
    if (c > d):
        d = c
    c = 0

for i in range(len(b[0])):
    for j in range(len(b)):
        e = b[j][i].count('9')
        c += e
    if (c > d):
        d = c
    c = 0

for i in range(len(b)):
    for j in range(len(b[0])):
        e = b[i][j].count('9')
        c += e

print(c-d)