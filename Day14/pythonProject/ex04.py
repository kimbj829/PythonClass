'''
* 서브 클래스(자식)가 슈퍼 클래스(부모)를 상속받으면
서브 클래스(자식)는 슈퍼 클래스(부모)의 변수, 메소드 기능들을 사용할 수 있다.
'''
class Person:               #부모 클래스
    def __init__(self, name):
        self.name = name;

    def eat(self, food):
        print(self.name + "가 " + food + "를 먹습니다.");


class Student(Person):      #자식 클래스(부모)
    def __init__(self,name, school):
        super().__init__(name);
        self.school = school;

    def study(self):
        print(self.name + "는 " + self.school + "에서 공부합니다.");


potter = Student("해리포터", "호그와트");
potter.eat("피자");
potter.study();