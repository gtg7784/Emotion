a = int(input())
b = []
c = 0

for i in range(a):
    z = input()
    b.append(z)

for i in range(len(b)):
    for j in range(0, 16, 2):
        c += int(b[i][j + 1:j + 2])
        y = int(b[i][j:j + 1])*2
        if y >= 10:
            c += int(str(y)[0]) + int(str(y)[1])
        else:
            c += y

    if (c % 10 == 0):
        print("T")
    else:
        print("F")
    
    c = 0