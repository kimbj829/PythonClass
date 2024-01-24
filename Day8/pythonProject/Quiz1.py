'''

컴퓨터가 1~100 숫자(정수 범위) 중 하나를 랜덤으로 정합니다. (이를 알려주지 않습니다.)
사용자는 이 숫자를 맞추어야 합니다.
입력한 숫자보다 정답이 크면 → "UP" 출력,
입력한 숫자보다 정답이 작으면 → "DOWN" 출력.
정답을 맞추면 → "정답"을 출력하고, 지금까지 숫자를 입력한 횟수를 알려줍니다.

(예시)
컴퓨터가 1~100 중 랜덤 숫자 하나를 정합니다.
이 숫자를 맞춰주세요.
1~100 숫자 입력:50
DOWN
1~100 숫자 입력:25
UP
1~100 숫자 입력:38
DOWN
1~100 숫자 입력:32
UP
1~100 숫자 입력:35
UP
1~100 숫자 입력:37
DOWN
1~100 숫자 입력:36
정답입니다! 7회 만에 맞췄어요.
'''
import random
num = random.randint(1,100);
#print(num);
count = 0;
print("컴퓨터가 1~100 중 랜덤 숫자 하나를 정합니다.");
print("이 숫자를 맞춰주세요.");

while True:
    answer = int(input("1~100 숫자 입력 : "));
    if 0 < answer <= 100 :
        if num == answer:
            count = count + 1;
            break;
        elif answer < num :
            count = count + 1;
            print("UP");
        else :
            print("DOWN");
            count = count + 1;
    else :
        #count = count + 1; #잘못된 입력도 횟수로 카운트 한다?
        print("Wrong input");

print("정답입니다. ! %d회 만에 맞췄습니다." %count);
