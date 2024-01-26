'''
매개 변수도 있고 반환값도 있는 함수
'''

def abs_function(number):
    if number < 0:
        return -number;
    else:
        return number;
print("-3의 절대값은 ?", abs_function(-3));
print("3의 절대값은 ?", abs_function(3));
