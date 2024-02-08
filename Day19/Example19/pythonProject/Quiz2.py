'''

두 정수 A와 B를 입력받은 다음
A + B를 출력하는 프로그램을 작성하세요
입력 마지막에 0 두개가 들어오면 프로그램을 종료 하고
입력받은 수의 A + B 계산 결과를 출력하세요
A와 B의 수의 범위는 (0 ~ 10) 사이임

실행결과)
입력 >> 1 1
입력 >> 2 3
입력 >> 3 4
입력 >> 9 8
입력 >> 5 2
입력 >> 0 0
[2, 5, 7, 17, 7]
'''

num_list = [];
while True:
    input_num = input("숫자를 입력하세요>> ").split();
    if input_num[0] == '0' and input_num[1] == '0':
        break;
    else:
        num1 = int(input_num[0]);
        num2 = int(input_num[1]);
        sum = num1 + num2;
        num_list.append(sum);
print(num_list);
'''
result = 0;
arr = [];
while True:
    num1, num2 = map(int, input("입력 >> ").split());
    if num1 == 0 and num2 == 0:
        break;
    result = num1 + num2;
    arr.append(result);
'''

