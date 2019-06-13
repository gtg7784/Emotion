a = []
for i in range(5):
    z = input()
    if len(z) != 15:
        for i in range((15 - len(z))):
            z += " "
    a.append(z)

for i in range(len(a[0])):
    for j in range(5):
        if (a[j][i] != " "):
            print(a[j][i], end='')