'''
주소록 프로젝트
1. 연락처 입력 (이름, 핸드폰번호, 이메일, 닉네임)
2. 연락처 출력
3. 연락처 삭제
4. 연락처 수정
5. 종료
'''
class Contact:
    def __init__(self, name, phone, email, nike): #초기 입력받은 정보를 생성
        self.name = name;
        self.phone = phone;
        self.email = email;
        self.nike = nike;
    def info(self):
        print("=======================");
        print("이름 :", self.name);
        print("연락처 :", self.phone);
        print("이메일 :", self.email);
        print("닉네임 :", self.nike);

# 입력함수
def set_contact():  #입력을 받는 함수 생성
    name = input("이름을 입력 >> ");
    phone = input("핸드폰 번호를 입력 >> ");
    email = input("이메일을 입력 >> ");
    nike = input("닉네임을 입력 >>");
    contact = Contact(name, phone, email, nike);    #입력받은 값을 인덱스에 생성
    return contact;
def print_contact(contact_list):    #contact_list에 있는 정보 호출 함수
    for item in contact_list:
        item.info();

# 연락처 삭제
def delete_contact(contact_list, name):
    for i, contact in enumerate(contact_list):
        if contact.name == name:
            del contact_list[i];
def update_contact(contact_list, phone):
    for i, contact in enumerate(contact_list):
        if contact.phone == phone:
            contact_list[i] = set_contact();

contact_list = [];

while True:
    print("1. 연락처 입력");
    print("2. 연락처 출력");
    print("3. 연락처 삭제");
    print("4. 연락처 수정");
    print("5. 종료");
    menu = int(input("메뉴 선택 >> "));

    if menu == 1:
        contact = set_contact();
        contact_list.append(contact);
    elif menu == 2:
        print_contact(contact_list);
    elif menu == 3:
        name = input("삭제할 이름 입력 >> ");
        delete_contact(contact_list, name);
    elif menu == 4:
        phone = input("수정할 전화번호를 입력하세요 >> ");
        update_contact(contact_list, phone);
    elif menu == 5:
        break;
    else :
        print("잘못된 입력입니다.");