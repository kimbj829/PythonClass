'''
중첩 if문
- if문 안에 또 다른 if문을 선언하여 중첩 if문을 만들 수 있다

형식)
if 조건식 :
    if 조건식 :
else :
    코드 ...
'''
x = int(input("숫자입력 : "));
if x > 0:
    if x < 10:
        print("x는 0보다 크고 10보다 작은 수 입니다.");
    else :
        print("x는 10이상의 수 입니다.");
else :
    print("x는 10보다 작은 수 입니다.");