'''
자료형
-int(변수), float(실수), complex(복소수), str(문자열), bool(논리)

'''

num1 = 10; #양의 정수
num2 = -10; #음의 정수
num3 = 0;
dd =0;
d1 = 1;
d2 = 2;

print(num1); print(num2); print(num3);
print(type(num1)); print(type(num2)); print(type(num3));

# 파이썬에서는 기본적으로 원하는 값을 크기에 제한없이 사용 가능함
num4 = 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999;
print(num4); print(type(num4));

# 10진수, 2진수, 8진수, 16진수
num1_int = 10;
print(bin(num1_int));
print(oct(num1_int));
print(hex(num1_int));

# 실수(float)
# 수소점이 있는 숫자를 실수라고 한다
num_float = 10.0;
print(num_float); print(type(num_float));
num1_float = 3.141592;
print(num1_float); print(type(num1_float));

# 문자열(str)
a_str = 'Good Student';
b_str = "Bad Student";
print(a_str); print(type(a_str));
print(b_str); print(type(b_str));

c_str = '''abc
df
asdf''';
print("c_str =", c_str); print(type(c_str));

# 논리(bool)
# True, False 값을 가질 수 있다
# 숫자 0, 빈 문자열, [] 빈 리스트 모두 False로 반환

a = 1; b = 0;
print("a =", bool(a)); print("b =",bool(b));
str1 = "";
print("str1 =",bool(str1));
list1 = [];
print("list1 =",bool(list1));

# 복소수(Complex)
# 실수와 허수부를 구분하여 표현할 수 있다.
a1 = 2 +3j;
print(type(a1)); print(a1);

# 기본적인 사칙연산
a1 = 20;
b1 = 3;
print("덧셈결과 :", (a1 + b1));
print("뺄셈결과 :", (a1 - b1));
print("곱셈결과 :", (a1 * b1));
print("나누셈 결과 :", (a1 / b1));
print("나눗셈 나머지 :", (a1 % b1));
print("나눗셈 몫만 출력 :", (a1 // b1));
print("2를 4번 제곱한 결과 :", (2 ** 4));
