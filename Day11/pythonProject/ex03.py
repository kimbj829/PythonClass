def myFunc(*args):
    for arg in args:
        print(arg);

myFunc(10,20,'a');
myFunc('apple', 'banana', 1.0, 10, 3.141592);
p1 = [10, 20, 30];
myFunc(p1);

print("=====================");

def total_sum(*args):
    sum = 0;
    for i in args:
        sum = sum + i;
    return sum;

# 입력받은 문자열을 공백을 기준으로 정수로 변환 후 리스트에 저장
num_list = list(map(int, input("숫자입력 >> ").split()));
print(num_list);
print(total_sum(*num_list));