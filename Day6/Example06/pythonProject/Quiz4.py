'''
A ~ Z 까지의 알파벳을 입력받아 대문자는 소문자로 소문자는 대문자로 변경하는 프로그램을 작성하세요

아스키코드표 참조 !!

ord() 함수 이용 : 문자의 유니코드 숫자 값을 리턴하는 함수
'''

alp = input("A~Z 까지의 알파벳을 입력하세요 : ");
if 'A' <= alp <= 'Z':
    alp = ord(alp) + 32;
    print(alp + 32);
elif 'a' <= alp <= 'z':
    alp = ord(alp) - 32;
    print(chr(alp));
else :
    print("잘못된 입력입니다.");
'''
if 65 <= ord(alp) <= 90:
    print(chr(ord(alp)+32));
elif 97 <= ord(alp) <= 122:
    print(chr(ord(alp)-32));
else :
    print("잘못된 입력입니다.");
'''