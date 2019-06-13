a = int(input())
b = []
c = 0

for i in range(a):
    z = input()
    b.append(z)

for i in range(len(b)):
    for j in range(0, 12, 2):
        c += int(b[i][j:j + 1])

        if int(b[i][j + 1:j + 2]) > 5:
            c += int(b[i][j + 1:j + 2]) * 2 % 10
            c += int(b[i][j + 1:j + 2]) * 2 / 10
        else:
            c += int(b[i][j + 1:j + 2])*2

    if c % 10 == 0:
        print("T")
    else:
        print("F")
            
    