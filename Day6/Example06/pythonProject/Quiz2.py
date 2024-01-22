'''
실행 결과와 같은 간단한 계산 기능을 수행하는 프로그램을 작성하세요

실행 예)
기능 선택
1. 더하기
2. 빼기
3. 곱하기
4. 나누기
계산기 기능을 선택하세요(1/2/3/4/) >> 3
천번째 숫자를 입력하세요 >> 5
두번쨰 숫자를 입력하세요 >> 10
5 * 10 = 50
'''
print("기능 선택");
print("1. 더하기");
print("2. 빼기");
print("3. 곱하기");
print("4. 나누기");

chose = int(input("계산기 기능을 선택하세요(1/2/3/4) : "));
if 0 < chose < 5:
    a = int(input("첫번째 숫자를 입력하세요 : "));
    b = int(input("두천째 숫자를 입력하세요 : "));
    if chose == 1:
        sum = a + b;
        print("{} + {} = {}".format(a, b, sum));
    elif chose == 2:
        sum = a - b;
        print("{} - {} = {}".format(a, b, sum));
    elif chose == 3:
        sum = a * b;
        print("{} x {} = {}".format(a, b, sum));
    else :
        sum = a / b;
        print("{} / {} = {}".format(a, b, sum));
else :
    print("잘못된 입력값입니다.");

'''
chose = int(input("계산기 기능을 선택하세요(1/2/3/4) : "));

if 0 < chose < 5:
    a = int(input("첫번째 숫자를 입력하세요 : "));
    b = int(input("두천째 숫자를 입력하세요 : "));
    if chose == 1:
        print("{} + {} = {}".format(a, b, a + b));
    elif chose == 2:
        print("{} - {} = {}".format(a, b, a - b));
    elif chose == 3:
        print("{} x {} = {}".format(a, b, a * b));
    else :
        print("{} / {} = {}".format(a, b, a / b));
else :
    print("잘못된 입력값입니다.");
'''