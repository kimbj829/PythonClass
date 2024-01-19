'''
* 다양한 조건을 판단하는 조건문

if 조건 A:
    A 조건이 참일 때 수행
elif 조건 B:
    B 조건이 참일 때 수행
else :
    모든 조건이 거짓일 때 수행
'''

menu = int(input("선택 : "));

if menu == 1 :
    print("콜라");
elif menu == 2:
    print("사이다");
elif menu == 3:
    print("환타");
elif menu == 4:
    print("커피");
else :
    print("메뉴를 잘못 입력하셨습니다.");