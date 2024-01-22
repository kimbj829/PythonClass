'''
아르바이트 주간 또는 야간 근무와 근무 시간을 입력받아
급여를 계산하는 프로그램을 작성하세요

주간근무 : 9500원
야간근무 : 주간시급 : 1.5
아르바이트 급여 계산 프로그램
* 시급
- 주근근무 : 9500원
- 야간근무 : 주간시급 * 1.5

실행 예)
1.(주간근무) 또는 2(야간근무)를 입력해주세요 >> 2
근무 시간을 입력해주세요 >> 5
5시간 동안 일한 야간 급여는 71250원 입니다.
'''
salary = 9500;
#n_work = d_work * 1.5;
work = int(input("1.(주간근무) 또는 2(야간근무)를 입력해주세요 : "));
if 0 < work < 3:
    time = float(input("근무 시간을 입력해주세요 : "));
    if (time *10 % 10) == 0: #소수점 확인용 if는 짝수시간/else는 소수점 시간있으면 출력
        if work == 1:
            print("{}시간 동안 일한 주간 급여는 {}원 입니다.".format(int(time), int(time*salary)));
        else :
            print("{}시간 동안 일한 야간 급여는 {}원 입니다.".format(int(time), int(time*salary*1.5)));
    else :
        if work == 1:
            print("{}시간 동안 일한 주간 급여는 {}원 입니다.".format(time, int(time*salary)));
        else :
            print("{}시간 동안 일한 야간 급여는 {}원 입니다.".format(time, int(time*salary*1.5)));

else :
    print("잘못된 입력값입니다.");