ty = input("+ - * /를 선택하세요")

if (ty == '+'):
    a, b = input("계산할 두 숫자를 공백으로 구분하여 입력하세요.").split()
    a = int(a)
    b = int(b)
    print("계산 결과는 다음과 같습니다.", a + b)
elif (ty == '-'):
    a, b = input("계산할 두 숫자를 공백으로 구분하여 입력하세요.").split()
    a = int(a)
    b = int(b)
    print("계산 결과는 다음과 같습니다.", a - b)
elif (ty == '*'):
    a, b = input("계산할 두 숫자를 공백으로 구분하여 입력하세요.").split()
    a = int(a)
    b = int(b)
    print("계산 결과는 다음과 같습니다.", a * b)
elif (ty == '/'):
    a, b = input("계산할 두 숫자를 공백으로 구분하여 입력하세요.").split()
    a = int(a)
    b = int(b)
    print("계산 결과는 다음과 같습니다.", a / b)