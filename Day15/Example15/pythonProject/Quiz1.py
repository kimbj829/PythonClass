'''
계산기 기능을 하느 Calculator 클래스를 만들고
덧셈, 뺄셈, 곱셈, 나눗셈 연산을 할 때마다 어떠한 연산을
몇번 수행했는지 출력하세요

덧셈 연산을 두번했다면 2
뺄셈 연산을 한번했다면 1

1. 덧셈, 2. 뺄셈 3. 곱셈 4. 나눗셈 5. 프로그램 종료
'''

class Calculator():

    def __init__(self):
        self.addCount = 0;
        self.minCount = 0;
        self.mulCount = 0;
        self.divCount = 0;

    def sum(self, num1, num2):
        self.addCount = self.addCount + 1;
        return num1 + num2;
    def sub(self, num1, num2):
        self.minCount = self.minCount + 1;
        return num1 - num2;
    def mul(self, num1, num2):
        self.mulCount = self.mulCount + 1;
        return num1 * num2;
    def div(self, num1, num2):
        self.divCount = self.divCount + 1;
        return num1 / num2;

    def info(self):
        print("덧셈 결과 : {}".format(self.addCount));
        print("뺄셈 결과는 : {}".format(self.minCount));
        print("곱셈 결과는 : {}".format(self.mulCount));
        print("나눗셈 결과는 : {}".format(self.divCount));

cal = Calculator();

while True:
    print("1. 덧셈, 2. 뺄셈 3. 곱셈 4. 나눗셈 5. 프로그램 종료");
    check = int(input("메뉴 선택 >> "));

    if 1 <= check <= 4:
        num1 = int(input("숫자를 입력하세요 >> "));
        num2 = int(input("숫자를 입력하세요 >> "));
        if check == 1:
            print(cal.sum(num1, num2));
        elif check == 2:
            print(cal.sub(num1, num2));
        elif check == 3:
            print(cal.mul(num1, num2));
        elif check == 4:
            print(cal.div(num1, num2));
    elif check == 5:
        cal.info();
        break;
    else :
        print("잘못된 입력입니다.");


'''

class Calculator():

    def __init__(self):
        self.addCount = 0;
        self.minCount = 0;
        self.mulCount = 0;
        self.divCount = 0;
        #입력값도 def로 받아온 버전
        self.num1 = 0;
        self.num2 = 0;
    def input_num(self):
        self.num1 = int(input("숫자를 입력하세요 >> "));
        self.num2 = int(input("숫자를 입력하세요 >> "));
    def sum(self):
        self.addCount = self.addCount + 1;
        return self.num1 + self.num2;
    def sub(self):
        self.minCount = self.minCount + 1;
        return self.num1 - self.num2;
    def mul(self):
        self.mulCount = self.mulCount + 1;
        return self.num1 * self.num2;
    def div(self):
        self.divCount = self.divCount + 1;
        return self.num1 / self.num2;

    def info(self):
        print("덧셈 결과 : {}".format(self.addCount));
        print("뺄셈 결과는 : {}".format(self.minCount));
        print("곱셈 결과는 : {}".format(self.mulCount));
        print("나눗셈 결과는 : {}".format(self.divCount));

cal = Calculator();

while True:
    print("1. 덧셈, 2. 뺄셈 3. 곱셈 4. 나눗셈 5. 프로그램 종료");
    check = int(input("메뉴 선택 >> "));
    if 1 <= check <= 4:
        cal.input_num();
        if check == 1:
            print(cal.sum());
        elif check == 2:
            print(cal.sub());
        elif check == 3:
            print(cal.mul());
        elif check == 4:
            print(cal.div());
    elif check == 5:
        cal.info();
        break;
    else :
        print("잘못된 입력입니다.");
'''

