'''
함수를 사용하세요
두 수를 입력받아 계산기 프로그램을 작성하세요
계산기 기능
1. 더하기
2. 빼기
3. 곱하기
4. 나누기(0으로 나누려 하면 0으로 나눌 수 없습니다 라고 출력)
5. 프로그램 종료
5번을 누르기 전까지는 각 메뉴를 입력받아 그에 해당하는 기능을 수행하도록 작성

'''
def add(a, b):
    return print("{} + {} = {}".format(a, b, a+b));
def sub(a, b):
    return print("{} - {} = {}".format(a, b, a-b));
def mul(a, b):
    return print("{} * {} = {}".format(a, b, a*b));
def div(a, b):
    if b == 0:
        print("0으로는 나눌수 없습니다.");
    else :
        return print("{} / {} = {}".format(a, b, a / b));
def num(choice):
    num1 = int(input("숫자를 입력해주세요 : "));
    num2 = int(input("숫자를 입력해주세요 : "));
    if choice == 1:
        add(num1, num2);
    elif choice == 2:
        sub(num1, num2);
    elif choice == 3:
        mul(num1, num2);
    else :
        div(num1, num2);
# def num(num1, num2):
#     num1 = int(input("숫자를 입력해주세요 : "));
#     num2 = int(input("숫자를 입력해주세요 : "));
#     return num1, num2;
while True:
    print("1.더하기 | 2. 빼기 | 3. 곱하기 | 4. 나누기 | 5. 프로그램 종료");
    choice = int(input("사용하실 기능을 선택해주세요: "));
    if 0 < choice < 5:
        num(choice);
    # if choice == 1:
    #     num(num1, num2);
    #     add(num1, num2);
    # elif choice == 2:
    #     pass;
    # elif choice == 3:
    #     pass;
    # elif choice == 4:
    #     pass;
    elif choice == 5 :
        print("프로그램 종료");
        break;
    else:
        print("잘못 입력하셨습니다.");
'''
def add(a, b):
    return a+b;
def sub(a, b):
    return a-b;
def mul(a, b):
    return a*b;
def div(a, b):
    if b == 0:
        print("0으로는 나눌수 없습니다.");
    else :
        return a//b;
while True:
    print("1.더하기 | 2. 빼기 | 3. 곱하기 | 4. 나누기 | 5. 프로그램 종료");
    choice = int(input("사용하실 기능을 선택해주세요: "));
    if choice == 1:
        num1 = int(input("숫자 입력 : "));
        num2 = int(input("숫자 입력 : "));
        print("덧셈결과 : ", add(num1, num2));
    elif choice == 2:
        num1 = int(input("숫자 입력 : "));
        num2 = int(input("숫자 입력 : "));
        print("뺄샘결과 : ", sub(num1, num2));
    elif choice == 3:
        num1 = int(input("숫자 입력 : "));
        num2 = int(input("숫자 입력 : "));
        print("곱셈결과 : ", mul(num1, num2));
    elif choice == 4:
        num1 = int(input("숫자 입력 : "));
        num2 = int(input("숫자 입력 : "));
        print("나눈셈 결과 : ", div(num1, num2));
    elif choice == 5 :
        print("프로그램 종료");
        break;
    else:
        print("잘못 입력하셨습니다.");
'''