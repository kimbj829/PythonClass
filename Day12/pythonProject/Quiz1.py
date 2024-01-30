'''
월을 입력받아 계절 이름이 출력되는 프로그램을 작성하세요(함수버전)
12,1,2 : 겨울
3, 4, 5 : 봄
6, 7, 8 : 여름
9, 10, 11 : 가을
'''

def spring():
    print("봄");
def summer():
    print("여름");
def fall():
    print("가을");
def winter():
    print("겨울");

'''
while True:
    month = int(input("월을 입력하세요 >> "));
    if 3 <= month <= 5:
        spring();
    elif 6<= month <= 8:
        summer();
    elif 9 <= month <= 11:
        fall();
    elif 12 == month or 1 <= month <= 2:
        winter();
    elif month == -1:
        print("프로그램 종료");
        break;
    else :
        ("잘못된 입력입니다.");

'''
def season(month):
    if 3 <= month <= 5:
        spring();
    elif 6<= month <= 8:
        summer();
    elif 9 <= month <= 11:
        fall();
    elif 12 == month or 1 <= month <= 2:
        winter();
    elif month == -1:
        return 0;
    else :
        print("잘못된 입력");

month = int(input("월을 입력하세요 >> "));
season(month);