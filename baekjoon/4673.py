a = set(range(1, 10000))
b = set()

for i in range(1, 10000):
    for j in str(i):
        i += int(j)
    b.add(i)

for i in sorted(a-b):
    print(i)