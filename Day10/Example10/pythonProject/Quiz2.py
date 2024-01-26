'''
세 개의 숫자를 입력받아 가장 큰 수를 출력하는 print_max 함수를 정의하고
가장 큰 수를 출력하세요
'''

def print_max(a, b, c):
    if a + b > a + c:
        if a > b:
            return a;
        else:
            return b;
    else:
        if a > c:
            return a;
        else:
            return c;

def max_num(a,b,c):
    return max(a,b,c);

num1 = int(input("숫자를 입력하세요 : "));
num2 = int(input("숫자를 입력하세요 : "));
num3 = int(input("숫자를 입력하세요 : "));

print("1. 가장 큰 숫자는", print_max(num1, num2, num3));
print("2. 가장 큰 숫자는", max(num1, num2, num3));
