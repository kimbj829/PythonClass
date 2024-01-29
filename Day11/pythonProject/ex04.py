'''
키워드 가변인자
- 키워드 파라미터를 사용할 떄는 매개변수 앞에 별 두개(**)를 붙힘
- 딕셔너리로 만들어 져서 출력이 된다
- kwargs(keyword argument)는 (key(키워드)) = values(값)) 형태로 함수를 호출할 수 있다
- 가독성을 위해 kwargs 그대로 사용하는 걸 권장

*(변수) : 여러개의 값이 들어올 때 함수 내부에서 해당 변수를 튜플로 처리
**(변수) : 키워드로 입력할 경우에는 그것을 각각 키와 값으로 가져오는 딕셔너리로 처리
'''

def name_and_age(**kwargs):
    print(kwargs);
    print(type(kwargs));

name_and_age(name='홍길동', age=50);
#name_and_age(10,20,30,40,50); # 이건 키값이 없어서 에러