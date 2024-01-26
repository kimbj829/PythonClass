'''
함수 내용만 있는 함수
'''

def sayHello():
    print("Hello");
    print("Python very very easy");
    print("good boy");
sayHello();
print("=============");

# 매개변수만 있는 함수
def signGood(when):
    if when == 1:
        print("Good Morning");
    elif when == 2:
        print("Good Afternoon");
    elif when ==3:
        print("Good Evening");
    else :
        print("Good Night");
signGood(1); signGood(2); signGood(3); signGood(4);
print("=============");

def hap(a,b): #외부에서 값을 받아 결과값을 출력
    result = a + b;
    print("전달받은 두 수의 합은 :", result);

hap(100, 200); # 함수 내부에 값을 보냄
#print(hap(100, 200)); # 이건 출력 불가(함수 내부에 return값이 없기 때문에)