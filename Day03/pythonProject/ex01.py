'''
print() 함수
- 출력할 문장을 '' 또는 ""로 감싸야 한다
- 콤마로 문자열을 나열할 경우 공백이 자동으로 추가된다.
- + 기호를 사용하여 문자열을 공백없이 연결할 수 있다.

print() 속성
- End 속성 : print 함수를 여러 줄을 써서 실행해보면 각각 줄바꿈이 되어 출력되는걸 확인할 수 있다.

Separator
- 출력할 데이터가 여럿이면 괄호 안에 출력할 데이터들을 print함수 내부에는 구분자로 불리는 sep 이라는 속성이 값들이 나란히 출력된다.
- 기본값으로 공백 문자열이 저정되어 있는데 sep 구문을 사용하여 변경가능

제어문자 종류
\n 줄바꿈, 개행문자
\t 띄워쓰기 tab
\\ : 역슬래시 표현
\" : "표현
\' : '표현
'''
'''
print("Hello,"+ "world");
print("Hello", "World");
'''

print("Python", end=' ');
print("Java", end = ' ');
print("C", end = ' ');
print("React", end = ' ');
print("\n");
#print();

print("========================");

print("Spring", end = ' ');
print("Spirng Boot", end = ' ');
print("Android");

print("========================");

print("자기소개", end='');
print("\n이름 : ", end= '');
print("윤준형\n나이 :", 150, "살");

print("나는\t", "학교에", "갑니다");

print("I\'am a good boy");
print("he said \"python is easy\"");

# sep 사용 예

print("Python", "Java", "C", sep = '-=-')
print("Python", "쉽다", sep = '은 엄청 ');