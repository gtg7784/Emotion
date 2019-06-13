a = int(input())
arr = []
alpha = set([])
result = []
count = 0
rescount = 0

for i in range(a):
    b = input()
    arr.append(b)
    arr[i] = arr[i][0:1]
    alpha.add(arr[i])

alpha = list(alpha)
alpha.sort()

for i in range(len(alpha)):
    for j in range(len(arr)):
        if alpha[i] == arr[j]:
            count += 1
        else:
            pass

    if count >= 5:
        print(alpha[i], end="")
        count = 0
        rescount += 1
    else:
        count = 0

if rescount == 0:
    print("PREDAJA")