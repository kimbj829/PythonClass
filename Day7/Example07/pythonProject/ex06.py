'''
continue문
- break문과 달리 반복문을 종료하는 것이 아니다
- continue문을 만나는 순간 continue문 아래에 있는 실행해야 하는 문장들을 건너 뛰고 다음 반복을 시작
'''

i = 0;
while i < 10:
    i = i + 1;
    if i % 2 == 0:
        continue;
    print(i);