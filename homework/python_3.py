def plus(a, b):
    return a + b
    
def minus(a, b):
    return a - b;

def division(a, b):
    return a / b
    
def multiply(a, b):
    return a * b
    
def remainder(a, b):
    return a % b
    
def exponentiation(a, b):
    return a ** b

def quotient(a, b):
    return a // b


def average(num_list):
    re = 0
    for i in num_list:
        re = re + int(i)
    return int(re) / len(num_list)


menu = int(input("1. 계산기\n2. 평균 구하기\n다른키를 누르면 나갈 수 있습니다.\n>"))

if (menu == 1):
    a, b, c = input("숫자 문자 숫자 형태로 식을 입력하세요. (문자는 다음과 같습니다. + - * ** / // %)\n>").split()
    if (b == '+'):
        print("결과 값은 {0} 입니다.".format(plus(int(a), int(c))))
    elif (b == '-'):
        print("결과 값은 {0} 입니다.".format(minus(int(a), int(c))))
    elif (b == '*'):
        print("결과 값은 {0} 입니다.".format(multiply(int(a), int(c))))
    elif (b == '/'):
        print("결과 값은 {0} 입니다.".format(division(int(a), int(c))))
    elif (b == '**'):
        print("결과 값은 {0} 입니다.".format(exponentiation(int(a), int(c))))
    elif (b == '//'):
        print("결과 값은 {0} 입니다.".format(quotient(int(a), int(c))))
elif (menu == 2):
    a = input("평균값을 구하고 싶은 모든 수를 띄어쓰기로 구분하여 입력하세요.").split()
    print("결과 값은 {0} 입니다.".format(average(a)))