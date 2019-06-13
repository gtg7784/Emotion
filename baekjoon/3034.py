a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

for i in range(a):
    d = int(input())
    if (b * b + c * c) >= d*d:
        print("DA")
    else:
        print("NE") 