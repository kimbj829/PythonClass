'''
while문을 이용해 두 개의 주사위를 던졌을 때 나오는 눈을 출력하고 눈의 합이 5가 아니면 계속 주사위를 던지고
눈의 합이 5이면 실행을 멈추세요
그리고 주사위의 눈의 합을 모두 출력하세요
'''

import random
sum = 0; i = 0;
while True:
    a = random.randint(1, 6);
    b = random.randint(1, 6);
    sum = sum + (a + b);
    i = i + 1;
    if a + b == 5:
        print("{}번째 주사위의 합은 {}".format(i, a + b));
        break;
    print("{}번째 주사위의 합은 {}".format(i, a+b));

print("총 {}번 굴린 주사위의 합은 {}".format(i, sum));
#print(random.randint(1, 6));