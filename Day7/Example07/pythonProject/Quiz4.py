'''
수를 입력받아서 입력받은 수의 총 합계를 구하시오
-1을 입젹하면 반복이 종료되고 현재까지 입력받은 수의 총 합계를 구하세요
'''
print("수를 입력하세요");
sum = 0;
while True:
    num = int(input());
    if num == -1:
        break;
    sum = sum + num;
print(sum);
