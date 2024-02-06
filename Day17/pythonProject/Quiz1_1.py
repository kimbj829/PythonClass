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
'''

# N개가 입력되면 거기서 -1개씩

def check_num(num):
    if num >= 10:
        return num - 10;
    else:
        return num;
def str_to_list():
    input_num = input("숫자를 입력하세요");
    for i in input_num:
        i = int(i);
        num_list.append(i);


num = int(input("길이를 입력하세요>> "));
num_list = [];
sum = 0;

str_to_list();

for i in range(0, num):
    list_num = num_list[i];
    sum = sum + check_num(list_num);

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