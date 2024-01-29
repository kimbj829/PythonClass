'''
2단부터 9단까지 메뉴 선택에 따라
구구단을 출력하는 프로그램을 만드세요
1. 홀수 구구단
2. 짝수 구구단
3. 프로그램 종료

'''
# def으로 odd와 even 나눈 버전

class inputnum():
    def setdata(sel, choice):
        sel.choice = int(input("숫자를 입력하세요 : "));
    def odd(sel):
        for i in range(1, 10, 2):
            print("%d단" %i);
            for j in range(1, 10, 1):
                print("{} * {} = {}".format(i, j, i * j));
    def even(sel):
        for i in range(2, 10, 2):
            print("%d단" %i);
            for j in range(1, 10, 1):
                print("{} * {} = {}".format(i, j, i * j));
while True:
    num = inputnum(); #inputnum()이라는 클래스를 불러올 num이라는 변수로 저장
    print("1. 홀수 구구단 | 2. 짝수 구구단 | 3. 프로그램 종료");
    num.setdata(int); #num에서 불러올 값을 세팅해주는 함수
    # num.setdata에 choice라는 변수에 저장된 값을 확인 후 일치하는 곳에 수행
    if num.choice == 1: 
        num.odd();
    elif num.choice == 2:
        num.even();
    elif num.choice == 3:
        print("프로그램 종료");
        break;
    else :
        print("잘못된 입력입니다.");

'''
2단부터 9단까지 메뉴 선택에 따라
구구단을 출력하는 프로그램을 만드세요
1. 홀수 구구단
2. 짝수 구구단
3. 프로그램 종료

'''
#def에 모든걸 부여한 상황
'''
class inputnum():
    def setdata(sel, num1):
        print("1. 홀수 구구단 | 2. 짝수 구구단 | 3. 프로그램 종료");
        sel.num1 = int(input("숫자를 입력하세요 : "));
    def check(sel):
        if sel.num1 == 1:
            for i in range(1, 10, 2):
                print("%d단" %i);
                for j in range(1, 10, 1):
                    print("{} * {} = {}".format(i, j, i * j));
        elif sel.num1 == 2:
            for i in range(2, 10, 2):
                print("%d단" %i);
                for j in range(1, 10, 1):
                    print("{} * {} = {}".format(i, j, i * j));
        elif sel.num1 == 3:
            print("프로그램 종료");
            exit();
        else :
            print("잘못된 입력입니다.");
            num.setdata(int);
            num.check();

num = inputnum();
while True:
    num.setdata(int);
    num.check();


'''