'''
리턴값
- 리턴값은 없을 수도 있고 하나 혹은 여러 값일 수 있다

return 문이 없는 함수는 None 값을 리턴한다
return 문은 하나의 객체만 돌려줄 수 있다

*함수는 실제로 하나의 값을 돌려주는게 원칙이나
파이썬은 리스트, 튜플, 딕셔너리등의 자료형에 여러값을 담아서 돌려 줄 수 있다.
'''
def returnTest():
    return 10,20,30,40,50;

def turnNone(value):
    x = value;

def turnSet(value):
    x = {value, value + 1, value +2};
    return x;
print(returnTest());
print(turnNone(10));
print(turnSet(10));