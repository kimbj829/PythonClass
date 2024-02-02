try :
    a = int(input("숫자 입력 >> "));
    b = int(input("숫자 입력 >> "));
    print("{} / {} = {}". format(a,b,(a/b)));
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.");
except ValueError:
    print("정수만 입력하세요.");