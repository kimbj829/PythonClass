'''
반복문
- 반복문이란 프로그램 내에서 똑같은 명령을 일정 횟수만큼 반복하여 수행하도록 제어하는 명령문이다
-for, while

while문

while문의 기본 구조

while <조건문>:
    <수행문장1>
    <수행문장2>
    <수행문장3>

'''
i = 0; #초기값 설정
while i < 10: # i가 10보다 작을 동안
    i = i + 1; #i의 값이 1씩 증가시킨다.
    print("Hello world를 %d번 찍었습니다." %i);

    if i == 10 :
        print("반복종료");


'''    
for a in range(1, 11, 1):
    print("2. Hello world를 %d번 찍었습니다." %a);
'''