a = input().split()
b, c, d, e = '', '', '', ''

for i in range(len(a[0])):
    if a[0][i:i + 1] == '5':
        b += '6'
        d += '5'
    elif a[0][i:i + 1] == '6':
        b += '6'
        d += '5'
    else:
        b += a[0][i:i + 1]
        d += a[0][i:i + 1]

for i in range(len(a[1])):
    if a[1][i:i + 1] == '5':
        c += '6'
        e += '5'
    elif a[1][i:i + 1] == '6':
        c += '6'
        e += '5'
    else:
        c += a[1][i:i + 1]
        e += a[1][i:i + 1]


print(int(d) + int(e), int(b) + int(c))