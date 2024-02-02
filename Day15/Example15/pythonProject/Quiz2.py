'''
학생 클래스를 만들고
이름, 나이, 성별, 거주지를 입력받아 출력하세요
'''

class Student:
    def __init__(self):
        self.name = str;
        self.age = int;
        self.gender = str;
        self.address = str;
    def input_info(self):
        self.name = input("이름을 입력하세요 >> ");
        self.age = input("나이를 입력하세요 >> ");
        self.gender = input("성별을 입력하세요 >> ");
        self.address = input("거주지를 입력하세요 >> ");
    def print_info(self):
        print("이름 :", self.name);
        print("나이 :", self.age);
        print("성별 :", self.gender);
        print("거주지 :", self.address);


student = Student();
student.input_info();
student.print_info();
