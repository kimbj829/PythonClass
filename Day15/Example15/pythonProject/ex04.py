'''
else ~ finally
try :
    코드...
except :
    코드...
else :
    예외가 발생하지 않았을 때 실행할 코드
finally :
    예외발생 여부와 상관없이 항상 실행
'''

try:
    a = int(input("숫자 입력 >> "));
    b = int(input("숫자 입력 >> "));
    result = a / b;
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.");
except ValueError:
    print("정수만 입력할 수 있습니다.");
else:
    print("{} / {} = {}".format(a, b, a/b));
finally:
    print("프로그램을 종료합니다.");