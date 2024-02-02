'''
예외처리
- 예외(Exception)란 코드를 실행하는 도중에 발생한 에러
- 에러가 발생하면 프로그램이 죽지 않도록 막아주는 역활

형식)
try :
    코드
except :
    코드

예)
while True:
    menu = int(input("나누기 프로그램 >> "));
    if menu == 1:
        print(4 / 0) #ZeroDivisionError: division by zero 분모에 0으로 불가라 while문 중에서도 프로그램이 종료
    elif menu == 2:
        break;

예)
a = 10;
b = 0;
result = a / b; #ZeroDivisionError: division by zero
print(result);
'''

a = 10;
b = 0;
try:
    result = a / b;
#except ZeroDivisionError <- 0으로 나눠지는 error에 한에 except후 밑의 코드를 실행
except: #except 조건 <- 조건이 없을경우 에러의 모든 케이스를 다 except로 받아버림
    print("0으로 나눌 수 없습니다.");