'''
세 개의 직선이 있다
숫자의 의미는 직선의 길이를 말한다
이 직선으로 삼각형을 만들 수 있는지 판단하는 프로그램을 작성하라
삼각형의 성립 조건)
a,b,c가 변의 길이이고 c가 제일 긴 길이라고 한다면
c < a + b 이면 삼각형이 성립된다.

입력 : 직선의 길이 3개가 입력으로 주어진다
출력 : 삼각형이 가능하면 "yes" 삼각형을 만들 수 없다면 "no"를 출력

입력 >> 2 3 4
출력 >> yes
'''
print("3개의 입력값을 입력하세요.");
a = int(input());
b = int(input());
c = int(input());

if c < a + b:
    print("yes");
else :
    print("No");
    
'''
print("3개의 입력값을 입력하세요.");
num_list = list(map(int, input().split()));
if num_list[2] < num_list[0] + num_list[1]:
    print("yes");
else :
    print("no");
'''


