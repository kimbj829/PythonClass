'''
while문을 활용하여 키보드로부터 입력된 데이터로 예금, 출금, 조회, 종료 가능을 제작하세요

=========================
1.예금|2.출금|3.잔금|4.종료|
=========================
>>
'''
acc = 0;

while True:
    print("==================================");
    print("1.예금 | 2. 출금 | 3. 잔금 | 4. 종료");
    print("==================================");
    num = int(input(">>"));

    if num == 1 :
        money = int(input("이체할 금액 >> "));
        acc = acc + money;
        print("예금액 :", money);
    elif num == 2 :
        money = int(input("출금할 금액 >> "));
        if money > acc:
            print("잔액이 부족합니다.");
        else :
            acc = acc - money;
    elif num == 3 :
        print("잔고 :", acc);

    elif num == 4 :
        print("프로그램을 종료합니다.");
        break;

    else :
        print("잘못된 입력값입니다.");

