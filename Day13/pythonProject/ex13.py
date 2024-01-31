class Person:
    '''
    파이썬에서 클래스 내부에서 메소드를 정의할 때 첫 번째 인자로  self를 사용

    *self
    인스턴스 자체를 가리키는 것(즉 나 자신)
    그 객체에 해당하는 메모리 번지를 가리킨다
    반드시 이 키워드를 써야지만 해당 객체로 접근할 수 있다
    객체 자기자신을 참조하는 매개변수
    ex)
    this.age = age; #java
    this -> age = age; #c++
    '''

    def sleep(self):
        print("잠잔다");

    def eat(self):
        print("먹는다");

    def run(self):
        print("달린다");

person1 = Person();
person2 = Person();

person1.sleep();
person1.run();
person1.eat();

person2.sleep();
person2.run();
person2.eat();
