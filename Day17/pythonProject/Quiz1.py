'''
N개의 숫자가 공백 없이 쓰여있다 이 숫자를 모두 합해서
출력하는 프로그램을 작성하세요

입력
첫째 줄에 숫자의 개수(1 <= N <= 100)이 주어진다
둘째 줄에 숫자 N개가 공백없이 주어진다
     N
입력) 1 1      출력)1
입력) 5 54321  출력)15
입력) 11 10987654321      출력) 46

#강사 풀이
n = int(input("입력 >> "));
number = input("입력 >> ");
sum = 0;
for i in range(n):
    sum = sum + int(number[i]);
print(sum);
'''

def check_num(num):
    if num >= 10:
        return num - 10;
    else :
        return num;

num = int(input("길이를 입력하세요>> "));
input_num = input("입력하세요 >> ");
num_list = [];

for i in input_num:
    i = int(i);
    num_list.append(i);

sum = 0;

for i in range(0, num):
    list_num = num_list[i];
    sum = sum + check_num(list_num);
print(sum);

'''
num = int(input("숫자를 입력하세요>> "));
sum = 0;

for i in range(num, 0, -1):
    if num >= 10:
        sum = sum + num - 10;
    else :
        sum = sum + num;
    num = num - 1;
    
print(sum);
'''


'''


sum = 0;

for i in range(num, 0, -1):
    sum = sum + check_num(num);
    num = num - 1;
print(sum);
'''
'''
def check_num(num):
    if num >= 10:
        return num - 10;
    else :
        return num;
        
num = int(input("숫자를 입력하세요>> "));
sum = 0;

while True:
    if num == 0:
        break;
    else :
        sum = sum + check_num(num);
        num = num -1;
print(sum);
'''
