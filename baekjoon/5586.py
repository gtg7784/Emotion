a = input()
b, c = 0, 0
for i in range(len(a)):
    if (a[i:i + 3] == 'JOI'):
        b += 1
    if (a[i:i + 3] == 'IOI'):
        c += 1
print(b)
print(c)
    