'''
and, or, not

and : x와 y 모두 참이면 참
or : x와 y 둘중 하나라도 참이면참
not : x가 거짓이면 참
'''

money = 2000;
card = True;

if money >= 30 or card:
    print("택시를 타고 가세요");
else :
    print("걸어 가세요");

pocket = ['paper', 'cellphone', 'money']

if 'money' in pocket: #pocket 라는 리스트에 money가 있냐?
    print("택시를 타고 가세요"); # 있으면 실행
else :
    print("걸어 가세요");    #없으면 실행
    
    