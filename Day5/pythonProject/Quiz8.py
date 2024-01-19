'''
두 정수 a와 b를 입력받아서
두 정수의 크기를 비교하여 왼쪽 수가 크면 >
오른쪽 수가 크면 <
같으면 = 를 출력
'''

num1 = int(input("정수를 입력해주세요 : "));
num2 = int(input("정수를 입력해주세요 : "));

if num1 > num2 :
    print ("{} > {}".format(num1, num2));
elif num1 < num2:
    print("{} < {}".format(num1, num2));
else :
    print("{} = {}".format(num1, num2));