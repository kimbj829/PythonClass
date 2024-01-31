'''
어느 직사각형의 정보를 출력하고 넓이를 구하는 클래스 만들기
'''

class Rectangle :
    # 필드(맴버변수) : 데이터를 표현하는 속성
    result = 0;
    width = 0;
    height = 0;

    #메소드 : 클래스의 어떠한 행위를 표현하는 것

    def arga(self):
        self.result = self.width * self.height;
        return self.result;

    def info(self):
        print("가로 길이는 : {}".format(self.width));
        print("세로 길이는 : {}".format(self.height));

rectangle = Rectangle();
width = int(input("가로입력 >> "));
height =int(input("세로입력 >> "));

#rectangle의 width라는 속성에 값을 할당
rectangle.width = width;
rectangle.height = height;
print("직사각형의 넓이 : ", rectangle.arga());
rectangle.info();