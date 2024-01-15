import keyword
'''
변수(Variable)
- 변수란 어떠한 값을 저장하고자 할 때 사용하는 메모리 공간
- 변수는 생성하는 즉시 어떠한 값을 넣어줘야 한다!!

변수 사용 예)
score = 10;

변수명 생성 규칙
- 영문 문자와 숫자를 사용한다.
- 변수는 대소문자를 구분한다.
- 문자부터 시작해야 하며 숫자부터 시작하면 안된다.
- _(밑줄문자)로 시작할 수 있다.
- 특수문자는 사용할 수 없다.
  (+, -, *, $, @, &, % 등)
- 파이썬의 키워드(if, for, while, and) 등은 사용할 수 없다.
- 변수명 이름은 가능한 표현하고자 하는 것을 완벽하고 정확하게 표현해야 한다.

* 키워드 : 어떤 기능을 하도록 미리 예약해 놓은 명령어

변수명 표기법
- 카멜 표기법, 파스칼 표기법, 형가리안 표기법, 팟홀 표기법

* 카멜 표기법(Camel Case)
예) carNumberName = "123가4567
- 각 단어의 첫 문자를 대문자로 표기하고 맨 처음 문자는 소문자로 표기함

* 파스칼 표기법(Pascal Case)
예) CarNumberName = "123가4567"
- 카멜표기법과 거의 흡사하지만 맨 처음 문자도 대문자로 표기함

* 헝가리안 표기법(Hungarian Notation)
예) strCarNumber = "123가4567"
    intAge = 20
- 데이터 타입을 명시하여 변수명을 작성하는 방법

*팟홀 표기법(Pothole Case)
예) car_number = 1111
- 단어 사이에 언더바를 넣어서 변수명을 작성하는 방법



'''
score = 10;
SCORE = 20;
print(type(score));
print(score);
print(SCORE);

score1 = 0;
print(type(score1));

_test = 200;


print(keyword.kwlist);