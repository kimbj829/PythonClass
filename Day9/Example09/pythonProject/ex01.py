'''
내장함수
- 파이썬에서 기본적으로 제공하는 함수
'''

# 숫자 내장 함수
# abs() : 전달된 인수(정수 또는 실수)의 절댓값을 반환
print(abs(10));
print(abs(-10));

# divmod() : 전달된 두 인수를 나누어 몫과 나머지를 한 쌍의 결과로 반환
result = divmod(8,5);
print(result); print(type(result));

print("==================");

# rount(); : 전달된 인수르 이용해 반올림한 값을 반환
print(round(1.5));
print(round(1.4));
print(round(1.55, 1));
# 대부분의 십진 소수가 float 형으로 정확히 표현될 수 없다
print(round(2.675, 2));

print("==================");
# ROUND_HALF_EVEN 방식
print(round(2.205, 2));
print(round(2.215, 2));
print(round(2.225, 2));
print(round(2.235, 2));
print(round(2.245, 2));